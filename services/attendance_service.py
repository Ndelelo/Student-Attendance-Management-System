from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Optional
from datetime import date

# Import your schemas (assuming you have these)
from domain.schemas.attendance import AttendanceCreate, AttendanceResponse, AttendanceUpdate

# Import your service and repository
from services.attendance_service import AttendanceService
from repositories.attendance_repository import AttendanceRepository
from database.database import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/attendances", tags=["attendances"])

# Dependency to get the repository and service
def get_attendance_repository(db: Session = Depends(get_db)):
    return AttendanceRepository(db)

def get_attendance_service(attendance_repository: AttendanceRepository = Depends(get_attendance_repository)):
    # Fixed: Using the correct parameter name 'attendance_repository' instead of 'repository'
    return AttendanceService(attendance_repository)

@router.post("/", response_model=AttendanceResponse, status_code=status.HTTP_201_CREATED)
def create_attendance(
    attendance: AttendanceCreate,
    service: AttendanceService = Depends(get_attendance_service)
):
    try:
        return service.mark_attendance(
            student_id=attendance.student_id,
            course_id=attendance.course_id,
            date=attendance.date,
            status=attendance.status
        )
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/", response_model=List[AttendanceResponse])
def get_attendance(
    student_id: Optional[int] = None,
    course_id: Optional[int] = None,
    date: Optional[date] = None,
    status: Optional[str] = None,
    service: AttendanceService = Depends(get_attendance_service)
):
    return service.get_attendance(
        student_id=student_id,
        course_id=course_id,
        date=date,
        status=status
    )

@router.get("/{attendance_id}", response_model=AttendanceResponse)
def get_attendance_by_id(
    attendance_id: int,
    service: AttendanceService = Depends(get_attendance_service)
):
    attendance = service.attendance_repository.find_by_id(attendance_id)
    if not attendance:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Attendance record with ID {attendance_id} not found"
        )
    return attendance

@router.put("/{attendance_id}", response_model=AttendanceResponse)
def update_attendance(
    attendance_id: int,
    attendance: AttendanceUpdate,
    service: AttendanceService = Depends(get_attendance_service)
):
    try:
        return service.update_attendance(
            attendance_id=attendance_id,
            student_id=attendance.student_id,
            course_id=attendance.course_id,
            date=attendance.date,
            status=attendance.status
        )
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

@router.delete("/{attendance_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_attendance(
    attendance_id: int,
    service: AttendanceService = Depends(get_attendance_service)
):
    try:
        service.delete_attendance(attendance_id)
        return None
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))