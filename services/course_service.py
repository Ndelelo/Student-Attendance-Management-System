# File: services/course_service.py
from domain.models.course import Course

class CourseService:
    def __init__(self, course_repository):
        """
        Initialize the course service
        
        Args:
            course_repository: Repository for course data
        """
        self.course_repository = course_repository
    
    def create_course(self, code, name, description=None, instructor=None):
        """
        Create a new course
        
        Args:
            code: Course code (e.g., "CS101")
            name: Name of the course
            description: Description of the course (optional)
            instructor: Name of the course instructor (optional)
            
        Returns:
            The created course record
            
        Raises:
            ValueError: If a course with the given code already exists
        """
        # Check if course code already exists
        existing = self.course_repository.find_by_code(code)
        if existing:
            raise ValueError(f"Course with code {code} already exists")
        
        # Create new course
        course = Course(
            id=None,  # Repository will assign ID
            code=code,
            name=name,
            description=description,
            instructor=instructor
        )
        
        # Save and return
        return self.course_repository.save(course)
    
    def get_course(self, course_id):
        """
        Get a course by ID
        
        Args:
            course_id: The ID of the course
            
        Returns:
            The course record if found
            
        Raises:
            ValueError: If the course does not exist
        """
        course = self.course_repository.find_by_id(course_id)
        if not course:
            raise ValueError(f"Course with ID {course_id} not found")
        
        return course
    
    def get_course_by_code(self, code):
        """
        Get a course by course code
        
        Args:
            code: The course code (e.g., "CS101")
            
        Returns:
            The course record if found
            
        Raises:
            ValueError: If the course does not exist
        """
        course = self.course_repository.find_by_code(code)
        if not course:
            raise ValueError(f"Course with code {code} not found")
        
        return course
    
    def search_courses_by_name(self, name):
        """
        Search for courses by name
        
        Args:
            name: The name to search for
            
        Returns:
            List of course records with names containing the search term
        """
        return self.course_repository.find_by_name(name)
    
    def get_all_courses(self):
        """
        Get all courses
        
        Returns:
            List of all course records
        """
        return self.course_repository.find_all()
    
    def update_course(self, course_id, code=None, name=None, description=None, instructor=None):
        """
        Update an existing course
        
        Args:
            course_id: The ID of the course to update
            code: New course code (optional)
            name: New name (optional)
            description: New description (optional)
            instructor: New instructor (optional)
            
        Returns:
            The updated course record
            
        Raises:
            ValueError: If the course does not exist or if the code is already used by another course
        """
        # Get existing course
        course = self.course_repository.find_by_id(course_id)
        if not course:
            raise ValueError(f"Course with ID {course_id} not found")
        
        # Check if code already exists (if provided and changed)
        if code and code != course.code:
            existing = self.course_repository.find_by_code(code)
            if existing and existing.id != course_id:
                raise ValueError(f"Course with code {code} already exists")
        
        # Update values if provided
        if code:
            course.code = code
        if name:
            course.name = name
        if description is not None:  # Allow empty description
            course.description = description
        if instructor is not None:  # Allow empty instructor
            course.instructor = instructor
        
        # Save and return
        return self.course_repository.save(course)
    
    def delete_course(self, course_id):
        """
        Delete a course
        
        Args:
            course_id: The ID of the course to delete
            
        Returns:
            True if deletion was successful
            
        Raises:
            ValueError: If the course does not exist
        """
        course = self.course_repository.find_by_id(course_id)
        if not course:
            raise ValueError(f"Course with ID {course_id} not found")
        
        return self.course_repository.delete(course_id)
