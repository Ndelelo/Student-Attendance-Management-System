# Changelog

## [Unreleased]
### Added
- Initial release of the API for managing student attendance records.

### Features
- **Student Management API**
  - `POST /students`: Create a new student record.
  - `GET /students`: Fetch all student records.
  - `GET /students/{id}`: Retrieve student details by ID.
  - `PUT /students/{id}`: Update student information by ID.
  - `DELETE /students/{id}`: Delete student record by ID.

- **Course Management API**
  - `POST /courses`: Create a new course.
  - `GET /courses`: Fetch all courses.
  - `GET /courses/{id}`: Retrieve course details by ID.
  - `PUT /courses/{id}`: Update course details by ID.
  - `DELETE /courses/{id}`: Delete a course by ID.

- **Attendance Management API**
  - `POST /attendance`: Record attendance for a student and a course.
  - `GET /attendance`: Fetch all attendance records.
  - `GET /attendance/{id}`: Retrieve attendance record by ID.
  - `GET /attendance/filter`: Filter attendance records by student, course, or date.

### Fixes
- Fixed issue with filtering attendance by date, which previously returned incorrect results.
- Fixed issue where creating a new student with an existing email would throw a server error instead of a validation error.

### Added
- **Basic API Structure**
  - Endpoints for adding, updating, and deleting students, courses, and attendance records.
  - Authentication endpoints (JWT-based) for securing API requests.

### Changed
- Updated the `POST /attendance` endpoint to ensure that attendance cannot be marked for a non-existent student or course.
- Refined the error messages for failed requests to improve clarity.

### Fixes
- Fixed incorrect HTTP status codes for `GET /students` when no records were found (previously returned 500, now returns 404).
- Fixed bug in the `PUT /students/{id}` endpoint where blank fields were not being handled correctly.

### Added
- Initial endpoints for managing student records:
  - `POST /students`: Create student.
  - `GET /students/{id}`: Get student by ID.

### Fixed
- Fixed `POST /students` endpoint validation to ensure the email is unique.
