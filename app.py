# app.py
from flask import Flask, request, jsonify, render_template, session, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import datetime, timedelta
import os
from functools import wraps

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///attendance.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    role = db.Column(db.String(20), nullable=False)  # Student, Teacher, Admin
    attendances = db.relationship('Attendance', backref='student', lazy=True, 
                                foreign_keys='Attendance.student_id')
    verified_attendances = db.relationship('Attendance', backref='verifier', lazy=True,
                                       foreign_keys='Attendance.verified_by')

class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.Date, default=datetime.utcnow)
    time = db.Column(db.Time, default=datetime.utcnow().time())
    status = db.Column(db.Boolean, default=True)  # True for Present, False for Absent
    verified = db.Column(db.Boolean, default=False)
    verified_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    note = db.Column(db.Text, nullable=True)

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    generated_date = db.Column(db.DateTime, default=datetime.utcnow)
    report_type = db.Column(db.String(50), nullable=False)  # Daily, Weekly, Monthly
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    file_path = db.Column(db.String(200), nullable=True)

# Authentication decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page', 'danger')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def role_required(*roles):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'role' not in session or session['role'] not in roles:
                flash('You do not have permission to access this page', 'danger')
                return redirect(url_for('dashboard'))
            return f(*args, **kwargs)
        return decorated_function
    return decorator

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        name = request.form['name']
        email = request.form['email']
        role = request.form['role']
        
        # Check if username or email already exists
        existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
        if existing_user:
            flash('Username or email already exists!', 'danger')
            return redirect(url_for('register'))
        
        # Hash the password
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        
        # Create new user
        new_user = User(username=username, password=hashed_password, name=name, email=email, role=role)
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        
        if user and bcrypt.check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['username'] = user.username
            session['name'] = user.name
            session['role'] = user.role
            
            flash(f'Welcome back, {user.name}!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Login failed. Please check your username and password.', 'danger')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    user_id = session['user_id']
    role = session['role']
    
    if role == 'Student':
        # Get student's recent attendance
        recent_attendance = Attendance.query.filter_by(student_id=user_id).order_by(Attendance.date.desc()).limit(10).all()
        
        # Calculate attendance percentage
        total_days = Attendance.query.filter_by(student_id=user_id).count()
        present_days = Attendance.query.filter_by(student_id=user_id, status=True).count()
        attendance_percentage = (present_days / total_days * 100) if total_days > 0 else 0
        
        return render_template('student_dashboard.html', 
                               recent_attendance=recent_attendance, 
                               attendance_percentage=attendance_percentage)
    
    elif role == 'Teacher':
        # Get attendance records that need verification
        unverified_attendance = Attendance.query.filter_by(verified=False).all()
        
        # Get list of students for attendance marking
        students = User.query.filter_by(role='Student').all()
        
        return render_template('teacher_dashboard.html', 
                               unverified_attendance=unverified_attendance,
                               students=students)
    
    elif role == 'Admin':
        # Get system statistics
        total_students = User.query.filter_by(role='Student').count()
        total_teachers = User.query.filter_by(role='Teacher').count()
        total_attendance_records = Attendance.query.count()
        recent_users = User.query.order_by(User.id.desc()).limit(5).all()
        
        return render_template('admin_dashboard.html', 
                               total_students=total_students,
                               total_teachers=total_teachers,
                               total_attendance_records=total_attendance_records,
                               recent_users=recent_users)

@app.route('/mark_attendance', methods=['GET', 'POST'])
@login_required
def mark_attendance():
    if request.method == 'POST':
        student_id = session['user_id'] if session['role'] == 'Student' else request.form['student_id']
        status = True  # Present
        note = request.form.get('note', '')
        
        # Check if attendance already marked for today
        today = datetime.utcnow().date()
        existing_attendance = Attendance.query.filter_by(student_id=student_id, date=today).first()
        
        if existing_attendance:
            flash('You have already marked your attendance for today!', 'warning')
        else:
            new_attendance = Attendance(
                student_id=student_id,
                date=today,
                time=datetime.utcnow().time(),
                status=status,
                note=note
            )
            db.session.add(new_attendance)
            db.session.commit()
            flash('Attendance marked successfully!', 'success')
        
        if session['role'] == 'Student':
            return redirect(url_for('dashboard'))
        else:
            return redirect(url_for('manage_attendance'))
    
    return render_template('mark_attendance.html')

@app.route('/verify_attendance/<int:attendance_id>', methods=['POST'])
@login_required
@role_required('Teacher', 'Admin')
def verify_attendance(attendance_id):
    attendance = Attendance.query.get_or_404(attendance_id)
    attendance.verified = True
    attendance.verified_by = session['user_id']
    db.session.commit()
    flash('Attendance verified successfully!', 'success')
    return redirect(url_for('manage_attendance'))

@app.route('/manage_attendance')
@login_required
@role_required('Teacher', 'Admin')
def manage_attendance():
    # Get filter parameters
    date_str = request.args.get('date')
    student_id = request.args.get('student_id')
    verified = request.args.get('verified')
    
    # Build query
    query = Attendance.query
    
    if date_str:
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
            query = query.filter_by(date=date)
        except ValueError:
            flash('Invalid date format!', 'danger')
    
    if student_id:
        query = query.filter_by(student_id=student_id)
    
    if verified is not None:
        verified_bool = (verified.lower() == 'true')
        query = query.filter_by(verified=verified_bool)
    
    attendances = query.order_by(Attendance.date.desc()).all()
    students = User.query.filter_by(role='Student').all()
    
    return render_template('manage_attendance.html', 
                           attendances=attendances, 
                           students=students)

@app.route('/generate_report', methods=['GET', 'POST'])
@login_required
@role_required('Teacher', 'Admin')
def generate_report():
    if request.method == 'POST':
        report_type = request.form['report_type']
        start_date_str = request.form['start_date']
        end_date_str = request.form.get('end_date')
        
        try:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            
            if end_date_str:
                end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
            else:
                if report_type == 'Daily':
                    end_date = start_date
                elif report_type == 'Weekly':
                    end_date = start_date + timedelta(days=6)
                elif report_type == 'Monthly':
                    # Approximate month end
                    if start_date.month == 12:
                        end_date = datetime(start_date.year + 1, 1, 1).date() - timedelta(days=1)
                    else:
                        end_date = datetime(start_date.year, start_date.month + 1, 1).date() - timedelta(days=1)
            
            new_report = Report(
                teacher_id=session['user_id'],
                report_type=report_type,
                start_date=start_date,
                end_date=end_date
            )
            db.session.add(new_report)
            db.session.commit()
            
            # In a real system, we would generate a PDF or CSV file here and save its path
            # For now, we'll just redirect to a report view
            
            flash('Report generated successfully!', 'success')
            return redirect(url_for('view_report', report_id=new_report.id))
        
        except ValueError:
            flash('Invalid date format!', 'danger')
    
    return render_template('generate_report.html')

@app.route('/view_report/<int:report_id>')
@login_required
@role_required('Teacher', 'Admin')
def view_report(report_id):
    report = Report.query.get_or_404(report_id)
    
    # Get attendance records for the report period
    attendances = Attendance.query.filter(
        Attendance.date >= report.start_date,
        Attendance.date <= report.end_date
    ).order_by(Attendance.date).all()
    
    # Group by student
    students = User.query.filter_by(role='Student').all()
    student_attendance = {}
    
    for student in students:
        student_attendance[student.id] = {
            'name': student.name,
            'present': 0,
            'absent': 0,
            'percentage': 0
        }
    
    for attendance in attendances:
        if attendance.student_id in student_attendance:
            if attendance.status:
                student_attendance[attendance.student_id]['present'] += 1
            else:
                student_attendance[attendance.student_id]['absent'] += 1
    
    # Calculate percentages
    for student_id, data in student_attendance.items():
        total = data['present'] + data['absent']
        if total > 0:
            data['percentage'] = round(data['present'] / total * 100, 2)
    
    return render_template('view_report.html', 
                           report=report, 
                           student_attendance=student_attendance,
                           attendances=attendances)

@app.route('/my_attendance')
@login_required
@role_required('Student')
def my_attendance():
    user_id = session['user_id']
    
    # Get all attendance records for the student
    attendances = Attendance.query.filter_by(student_id=user_id).order_by(Attendance.date.desc()).all()
    
    # Calculate statistics
    total_days = len(attendances)
    present_days = sum(1 for a in attendances if a.status)
    absent_days = total_days - present_days
    attendance_percentage = (present_days / total_days * 100) if total_days > 0 else 0
    
    return render_template('my_attendance.html', 
                           attendances=attendances,
                           total_days=total_days,
                           present_days=present_days,
                           absent_days=absent_days,
                           attendance_percentage=attendance_percentage)

@app.route('/user_management')
@login_required
@role_required('Admin')
def user_management():
    users = User.query.all()
    return render_template('user_management.html', users=users)

@app.route('/edit_user/<int:user_id>', methods=['GET', 'POST'])
@login_required
@role_required('Admin')
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    
    if request.method == 'POST':
        user.name = request.form['name']
        user.email = request.form['email']
        user.role = request.form['role']
        
        if request.form.get('password'):
            user.password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
        
        db.session.commit()
        flash('User updated successfully!', 'success')
        return redirect(url_for('user_management'))
    
    return render_template('edit_user.html', user=user)

@app.route('/delete_user/<int:user_id>', methods=['POST'])
@login_required
@role_required('Admin')
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    
    # In a real system, we might want to handle related records or soft delete
    # For this example, we'll just delete the user
    db.session.delete(user)
    db.session.commit()
    
    flash('User deleted successfully!', 'success')
    return redirect(url_for('user_management'))

# API endpoints for potential mobile app or integration
@app.route('/api/login', methods=['POST'])
def api_login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    user = User.query.filter_by(username=username).first()
    
    if user and bcrypt.check_password_hash(user.password, password):
        return jsonify({
            'success': True,
            'user_id': user.id,
            'name': user.name,
            'role': user.role
        })
    else:
        return jsonify({
            'success': False,
            'message': 'Invalid credentials'
        }), 401

@app.route('/api/mark_attendance', methods=['POST'])
def api_mark_attendance():
    data = request.json
    student_id = data.get('student_id')
    status = data.get('status', True)
    note = data.get('note', '')
    
    # Check if attendance already marked for today
    today = datetime.utcnow().date()
    existing_attendance = Attendance.query.filter_by(student_id=student_id, date=today).first()
    
    if existing_attendance:
        return jsonify({
            'success': False,
            'message': 'Attendance already marked for today'
        }), 400
    
    new_attendance = Attendance(
        student_id=student_id,
        date=today,
        time=datetime.utcnow().time(),
        status=status,
        note=note
    )
    db.session.add(new_attendance)
    db.session.commit()
    
    return jsonify({
        'success': True,
        'message': 'Attendance marked successfully',
        'attendance_id': new_attendance.id
    })

@app.route('/api/attendance_records', methods=['GET'])
def api_attendance_records():
    student_id = request.args.get('student_id')
    date_str = request.args.get('date')
    
    query = Attendance.query
    
    if student_id:
        query = query.filter_by(student_id=student_id)
    
    if date_str:
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
            query = query.filter_by(date=date)
        except ValueError:
            return jsonify({
                'success': False,
                'message': 'Invalid date format'
            }), 400
    
    records = query.all()
    
    return jsonify({
        'success': True,
        'records': [{
            'id': rec.id,
            'student_id': rec.student_id,
            'date': rec.date.strftime('%Y-%m-%d'),
            'time': rec.time.strftime('%H:%M:%S'),
            'status': rec.status,
            'verified': rec.verified,
            'verified_by': rec.verified_by,
            'note': rec.note
        } for rec in records]
    })

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)