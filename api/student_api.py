from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional

# Create router
router = APIRouter()

# Student model
class StudentBase(BaseModel):
    name: str
    email: str
    student_id: str

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int
    
    class Config:
        orm_mode = True

# In-memory student database for demo
students_db = [
    {"id": 1, "name": "John Doe", "email": "john@example.com", "student_id": "ST001"},
    {"id": 2, "name": "Jane Smith", "email": "jane@example.com", "student_id": "ST002"},
    {"id": 3, "name": "Bob Johnson", "email": "bob@example.com", "student_id": "ST003"}
]

# API endpoints
@router.get("/", response_model=List[Student])
def get_students():
    return students_db

@router.get("/{student_id}", response_model=Student)
def get_student(student_id: int):
    for student in students_db:
        if student["id"] == student_id:
            return student
    raise HTTPException(status_code=404, detail="Student not found")

@router.post("/", response_model=Student)
def create_student(student: StudentCreate):
    new_id = max(s["id"] for s in students_db) + 1 if students_db else 1
    new_student = {"id": new_id, **student.dict()}
    students_db.append(new_student)
    return new_student

@router.put("/{student_id}", response_model=Student)
def update_student(student_id: int, student: StudentBase):
    for i, s in enumerate(students_db):
        if s["id"] == student_id:
            students_db[i] = {**s, **student.dict()}
            return students_db[i]
    raise HTTPException(status_code=404, detail="Student not found")

@router.delete("/{student_id}")
def delete_student(student_id: int):
    global students_db
    students_db = [s for s in students_db if s["id"] != student_id]
    return {"message": "Student deleted successfully"}