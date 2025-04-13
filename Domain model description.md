# Domain model description

---

# Key Domain Entities

## 1. Student

**Attributes:**
- `studentId` (String)
- `name` (String)
- `email` (String)
- `rollNumber` (String)
- `department` (String)

**Responsibilities:**
- View attendance
- Update profile

**Relationships:**
- Enrolled in one or more **Courses**
- Has many **AttendanceRecords**

---

## 2. Course

**Attributes:**
- `courseId` (String)
- `courseName` (String)
- `department` (String)
- `teacherId` (String)

**Responsibilities:**
- Maintain course schedule
- Generate course-wise attendance report

**Relationships:**
- Taught by a **Teacher**
- Has many **Students**
- Linked to many **AttendanceRecords**

---

## 3. Teacher

**Attributes:**
- `teacherId` (String)
- `name` (String)
- `email` (String)
- `department` (String)

**Responsibilities:**
- Record attendance
- View and generate attendance reports

**Relationships:**
- Teaches multiple **Courses**

---

## 4. AttendanceRecord

**Attributes:**
- `recordId` (String)
- `date` (Date)
- `studentId` (String)
- `courseId` (String)
- `status` (Enum: Present, Absent, Late, Excused)

**Responsibilities:**
- Log and update attendance
- Track attendance status for a student in a course on a specific date

**Relationships:**
- Associated with a specific **Student** and **Course**

---

## 5. Schedule

**Attributes:**
- `scheduleId` (String)
- `courseId` (String)
- `dayOfWeek` (String)
- `startTime` (Time)
- `endTime` (Time)

**Responsibilities:**
- Maintain when and where a class meets

**Relationships:**
- Linked to a single **Course**

---

## 6. Department

**Attributes:**
- `departmentId` (String)
- `departmentName` (String)

**Responsibilities:**
- Manage course and student associations

**Relationships:**
- Has many **Students**, **Teachers**, and **Courses**
