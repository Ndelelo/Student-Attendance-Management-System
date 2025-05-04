from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from datetime import date

from services.attendance_service import AttendanceService
from domain.models.attendance import Attendance
from repositories.inmemory.attendance_repository import InMemoryAttendanceRepository  # ✅ Added

# Initialize repository and service properly
attendance_repository = InMemoryAttendanceRepository()
attendance_service = AttendanceService(repository=attendance_repository)

router = APIRouter()
templates = Jinja2Templates(directory="templates")

class AttendanceRequest(BaseModel):
    student_id: str
    course_id: str
    date: date

@router.post("/")
def mark_attendance(data: AttendanceRequest):
    if attendance_service.attendance_exists(data.student_id, data.course_id, data.date):
        raise HTTPException(status_code=400, detail="Attendance already marked")
    
    record = Attendance(
        student_id=data.student_id,
        course_id=data.course_id,
        date=data.date
    )
    attendance_service.mark_attendance(record)
    return {"message": "Attendance recorded"}

@router.get("/")
def list_attendance():
    return attendance_service.get_all_attendance()

@router.get("/student/{student_id}")
def get_attendance_by_student(student_id: str):
    return attendance_service.get_attendance_by_student(student_id)

@router.get("/course/{course_id}")
def get_attendance_by_course(course_id: str):
    return attendance_service.get_attendance_by_course(course_id)

# ✅ HTML Endpoint
@router.get("/html", response_class=HTMLResponse)
def attendance_html(request: Request):
    records = attendance_service.get_all_attendance()
    return templates.TemplateResponse("attendance.html", {"request": request, "attendance": records})
