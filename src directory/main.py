class Department:
    def __init__(self, department_id, department_name):
        self._department_id = department_id
        self._department_name = department_name
        self._courses = []
        self._members = []

    def manage_courses(self):
        pass

    def manage_members(self):
        pass


class Student:
    def __init__(self, student_id, name, email, roll_number, department):
        self._student_id = student_id
        self._name = name
        self._email = email
        self._roll_number = roll_number
        self._department = department
        self._courses = []
        self._attendance_records = []

    def view_attendance(self):
        return self._attendance_records

    def update_profile(self, name=None, email=None):
        if name:
            self._name = name
        if email:
            self._email = email


class Teacher:
    def __init__(self, teacher_id, name, email, department):
        self._teacher_id = teacher_id
        self._name = name
        self._email = email
        self._department = department
        self._courses = []

    def record_attendance(self, course, student, date, status):
        if course in self._courses:
            record = AttendanceRecord(course, student, date, status)
            student._attendance_records.append(record)

    def view_reports(self):
        pass


class Course:
    def __init__(self, course_id, course_name, department, teacher):
        self._course_id = course_id
        self._course_name = course_name
        self._department = department
        self._teacher = teacher
        self._students = []
        self._schedule = []

    def generate_attendance_report(self):
        pass


class Schedule:
    def __init__(self, schedule_id, day_of_week, start_time, end_time):
        self._schedule_id = schedule_id
        self._day_of_week = day_of_week
        self._start_time = start_time
        self._end_time = end_time

    def get_schedule(self):
        return {
            "day": self._day_of_week,
            "start": self._start_time,
            "end": self._end_time
        }


class AttendanceRecord:
    def __init__(self, course, student, date, status):
        self._record_id = f"{student._student_id}_{course._course_id}_{date}"
        self._date = date
        self._status = status
        self._student = student
        self._course = course

    def log_attendance(self):
        pass

    def update_attendance(self, status):
        self._status = status


if __name__ == "__main__":
    dept = Department("D001", "Computer Science")
    teacher = Teacher("T001", "Dr. Smith", "smith@example.com", dept)
    student = Student("S001", "Alice", "alice@example.com", "R123", dept)
    course = Course("C001", "OOP", dept, teacher)

    teacher._courses.append(course)
    course._students.append(student)
    student._courses.append(course)

    teacher.record_attendance(course, student, "2025-04-15", "Present")

    for record in student.view_attendance():
        print(f"Date: {record._date}, Status: {record._status}")
