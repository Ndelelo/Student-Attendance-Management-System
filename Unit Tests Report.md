# Unit Tests Report

## Overview

This report summarizes the results of the unit tests for the business logic of the Student Attendance Management System. The tests were conducted using `pytest` on 03-May-2025 at 23:35:37, and the report was generated with `pytest-html` v4.1.1.

## Environment

- **Python**: 3.13.1
- **Platform**: Windows-10-10.0.19045-SP0
- **Packages**:
  - `pytest`: 8.3.5
  - `pluggy`: 1.5.0
- **Plugins**:
  - `anyio`: 4.9.0
  - `html`: 4.1.1
  - `metadata`: 3.1.1

## Test Summary

- **Total tests**: 29
- **Duration**: 14 ms
- **Results**:
  - **Passed**: 29
  - **Failed**: 0
  - **Skipped**: 0
  - **Expected Failures**: 0
  - **Unexpected Passes**: 0
  - **Errors**: 0
  - **Reruns**: 0

## Detailed Results

| Test | Result | Duration |
|------|--------|----------|
| `tests/test_attendance_service.py::TestAttendanceService::test_get_attendance_by_student_and_course` | Passed | 1 ms |
| `tests/test_attendance_service.py::TestAttendanceService::test_mark_attendance_duplicate` | Passed | 1 ms |
| `tests/test_attendance_service.py::TestAttendanceService::test_mark_attendance_success` | Passed | 1 ms |
| `tests/test_course_service.py::TestCourseService::test_create_course_duplicate_code` | Passed | 1 ms |
| `tests/test_course_service.py::TestCourseService::test_create_course_success` | Passed | 1 ms |
| `tests/test_course_service.py::TestCourseService::test_delete_course` | Passed | 1 ms |
| `tests/test_course_service.py::TestCourseService::test_delete_course_not_found` | Passed | 1 ms |
| `tests/test_course_service.py::TestCourseService::test_get_all_courses` | Passed | 0 ms |
| `tests/test_course_service.py::TestCourseService::test_get_course_by_code` | Passed | 0 ms |
| `tests/test_course_service.py::TestCourseService::test_get_course_by_code_not_found` | Passed | 0 ms |
| `tests/test_course_service.py::TestCourseService::test_get_course_by_id` | Passed | 0 ms |
| `tests/test_course_service.py::TestCourseService::test_get_course_not_found` | Passed | 0 ms |
| `tests/test_course_service.py::TestCourseService::test_search_courses_by_name` | Passed | 0 ms |
| `tests/test_course_service.py::TestCourseService::test_update_course` | Passed | 0 ms |
| `tests/test_course_service.py::TestCourseService::test_update_course_duplicate_code` | Passed | 0 ms |
| `tests/test_course_service.py::TestCourseService::test_update_course_not_found` | Passed | 1 ms |
| `tests/test_student_service.py::TestStudentService::test_create_student_duplicate_email` | Passed | 1 ms |
| `tests/test_student_service.py::TestStudentService::test_create_student_duplicate_id` | Passed | 0 ms |
| `tests/test_student_service.py::TestStudentService::test_create_student_success` | Passed | 0 ms |
| `tests/test_student_service.py::TestStudentService::test_delete_student` | Passed | 0 ms |
| `tests/test_student_service.py::TestStudentService::test_delete_student_not_found` | Passed | 0 ms |
| `tests/test_student_service.py::TestStudentService::test_get_all_students` | Passed | 0 ms |
| `tests/test_student_service.py::TestStudentService::test_get_student_by_id` | Passed | 0 ms |
| `tests/test_student_service.py::TestStudentService::test_get_student_by_student_id` | Passed | 0 ms |
| `tests/test_student_service.py::TestStudentService::test_get_student_by_student_id_not_found` | Passed | 0 ms |
| `tests/test_student_service.py::TestStudentService::test_get_student_not_found` | Passed | 1 ms |
| `tests/test_student_service.py::TestStudentService::test_update_student` | Passed | 0 ms |
| `tests/test_student_service.py::TestStudentService::test_update_student_duplicate_email` | Passed | 0 ms |
| `tests/test_student_service.py::TestStudentService::test_update_student_not_found` | Passed | 0 ms |

## Visual Report

![Unit Tests Report](Unit%20tests.JPG)

## Conclusion

All 29 unit tests have passed successfully, indicating that the business logic of the Student Attendance Management System is functioning as expected.
