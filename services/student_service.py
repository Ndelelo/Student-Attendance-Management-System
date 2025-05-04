# File: services/student_service.py
from domain.models.student import Student

class StudentService:
    def __init__(self, student_repository):
        """
        Initialize the student service
        
        Args:
            student_repository: Repository for student data
        """
        self.student_repository = student_repository
    
    def create_student(self, student_id, name, email=None, phone=None):
        """
        Create a new student
        
        Args:
            student_id: Student ID number (e.g., "S001")
            name: Full name of the student
            email: Email address of the student (optional)
            phone: Phone number of the student (optional)
            
        Returns:
            The created student record
            
        Raises:
            ValueError: If a student with the given student ID or email already exists
        """
        # Check if student ID already exists
        existing = self.student_repository.find_by_student_id(student_id)
        if existing:
            raise ValueError(f"Student with ID {student_id} already exists")
        
        # Check if email already exists (if provided)
        if email:
            existing = self.student_repository.find_by_email(email)
            if existing:
                raise ValueError(f"Student with email {email} already exists")
        
        # Create new student
        student = Student(
            id=None,  # Repository will assign ID
            student_id=student_id,
            name=name,
            email=email,
            phone=phone
        )
        
        # Save and return
        return self.student_repository.save(student)
    
    def get_student(self, student_id):
        """
        Get a student by ID
        
        Args:
            student_id: The ID of the student
            
        Returns:
            The student record if found
            
        Raises:
            ValueError: If the student does not exist
        """
        student = self.student_repository.find_by_id(student_id)
        if not student:
            raise ValueError(f"Student with ID {student_id} not found")
        
        return student
    
    def get_student_by_student_id(self, external_student_id):
        """
        Get a student by external student ID (e.g., "S001")
        
        Args:
            external_student_id: The external student ID
            
        Returns:
            The student record if found
            
        Raises:
            ValueError: If the student does not exist
        """
        student = self.student_repository.find_by_student_id(external_student_id)
        if not student:
            raise ValueError(f"Student with student ID {external_student_id} not found")
        
        return student
    
    def get_all_students(self):
        """
        Get all students
        
        Returns:
            List of all student records
        """
        return self.student_repository.find_all()
    
    def update_student(self, student_id, name=None, email=None, phone=None):
        """
        Update an existing student
        
        Args:
            student_id: The ID of the student to update
            name: New name (optional)
            email: New email (optional)
            phone: New phone (optional)
            
        Returns:
            The updated student record
            
        Raises:
            ValueError: If the student does not exist or if the email is already used by another student
        """
        # Get existing student
        student = self.student_repository.find_by_id(student_id)
        if not student:
            raise ValueError(f"Student with ID {student_id} not found")
        
        # Check if email already exists (if provided and changed)
        if email and email != student.email:
            existing = self.student_repository.find_by_email(email)
            if existing and existing.id != student_id:
                raise ValueError(f"Student with email {email} already exists")
        
        # Update values if provided
        if name:
            student.name = name
        if email:
            student.email = email
        if phone:
            student.phone = phone
        
        # Save and return
        return self.student_repository.save(student)
    
    def delete_student(self, student_id):
        """
        Delete a student
        
        Args:
            student_id: The ID of the student to delete
            
        Returns:
            True if deletion was successful
            
        Raises:
            ValueError: If the student does not exist
        """
        student = self.student_repository.find_by_id(student_id)
        if not student:
            raise ValueError(f"Student with ID {student_id} not found")
        
        return self.student_repository.delete(student_id)
