from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional
from datetime import date

# Create router
router = APIRouter()

# Attendance model
class AttendanceBase(BaseModel):
    student_id: int
    course_id: int
    date: date
    status: str  # "present", "absent", "late"

class AttendanceCreate(AttendanceBase):
    pass

class Attendance(AttendanceBase):
    id: int
    
    class Config:
        orm_mode = True

# In-memory attendance database for demo
attendance_db = [
    {"id": 1, "student_id": 1, "course_id": 1, "date": date(2023, 5, 1), "status": "present"},
    {"id": 2, "student_id": 2, "course_id": 1, "date": date(2023, 5, 1), "status": "absent"},
    {"id": 3, "student_id": 3, "course_id": 1, "date": date(2023, 5, 1), "status": "present"},
    {"id": 4, "student_id": 1, "course_id": 2, "date": date(2023, 5, 2), "status": "present"},
    {"id": 5, "student_id": 2, "course_id": 2, "date": date(2023, 5, 2), "status": "present"}
]

# API endpoints
@router.get("/", response_model=List[Attendance])
def get_attendance(
    student_id: Optional[int] = None,
    course_id: Optional[int] = None,
    start_date: Optional[date] = None,
    end_date: Optional[date] = None
):
    results = attendance_db
    
    if student_id:
        results = [a for a in results if a["student_id"] == student_id]
    if course_id:
        results = [a for a in results if a["course_id"] == course_id]
    if start_date:
        results = [a for a in results if a["date"] >= start_date]
    if end_date:
        results = [a for a in results if a["date"] <= end_date]
        
    return results

@router.get("/{attendance_id}", response_model=Attendance)
def get_attendance_by_id(attendance_id: int):
    for attendance in attendance_db:
        if attendance["id"] == attendance_id:
            return attendance
    raise HTTPException(status_code=404, detail="Attendance record not found")

@router.post("/", response_model=Attendance)
def create_attendance(attendance: AttendanceCreate):
    # No need for global as we're only reading and appending, not reassigning
    new_id = max(a["id"] for a in attendance_db) + 1 if attendance_db else 1
    new_attendance = {"id": new_id, **attendance.dict()}
    attendance_db.append(new_attendance)
    return new_attendance

@router.put("/{attendance_id}", response_model=Attendance)
def update_attendance(attendance_id: int, attendance: AttendanceBase):
    for i, a in enumerate(attendance_db):
        if a["id"] == attendance_id:
            attendance_db[i] = {**a, **attendance.dict()}
            return attendance_db[i]
    raise HTTPException(status_code=404, detail="Attendance record not found")

@router.delete("/{attendance_id}")
def delete_attendance(attendance_id: int):
    # We're modifying the list in place, not reassigning, so no global needed
    original_length = len(attendance_db)
    attendance_db[:] = [a for a in attendance_db if a["id"] != attendance_id]
    if len(attendance_db) == original_length:
        raise HTTPException(status_code=404, detail="Attendance record not found")
    return {"message": "Attendance record deleted successfully"}

# Batch update attendance
@router.post("/batch")
def batch_create_attendance(attendances: List[AttendanceCreate]):
    # No need for global as we're only appending, not reassigning
    results = []
    
    for attendance in attendances:
        new_id = max(a["id"] for a in attendance_db) + 1 if attendance_db else 1
        new_attendance = {"id": new_id, **attendance.dict()}
        attendance_db.append(new_attendance)
        results.append(new_attendance)
        
    return {"message": f"Created {len(results)} attendance records", "records": results}
