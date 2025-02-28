## C1: Context Diagram
### Student Attendance Management System

```mermaid
graph TD;
    subgraph External Users
        Student[Student] -->|Marks Attendance| AttendanceSystem
        Teacher[Teacher] -->|Verifies Attendance| AttendanceSystem
        Admin[Admin] -->|Manages System| AttendanceSystem
    end
    
    subgraph External Services
        EmailService[Email Notification Service] -->|Sends Notifications| AttendanceSystem
    end
    
    AttendanceSystem[Student Attendance System] -->|Stores Data| Database[(Database)]
```

### Explanation:
- **Users:**
  - **Students** mark their attendance.
  - **Teachers** verify student attendance.
  - **Admins** manage users and system configurations.
- **External Services:**
  - **Email Service** sends attendance reports.
- **System Interactions:**
  - The **Attendance System** stores and retrieves attendance records from the **database**.

---

## C2: Container Diagram
### System Components

```mermaid
graph TD;
    subgraph AttendanceSystem
        WebApp[Web Application] -->|Requests| Backend[Backend API]
        Backend -->|Reads/Writes| Database[(Database)]
        Backend -->|Sends Notifications| EmailService[Email Service]
    end

    Student[Student] -->|Uses| WebApp
    Teacher[Teacher] -->|Manages| WebApp
    Admin[Admin] -->|Configures| WebApp
```

### Explanation:
- **Web Application:** Interface for users to interact with the system.
- **Backend API:** Handles logic and data processing.
- **Database:** Stores student attendance records.
- **Email Service:** Sends attendance reports.

---

## C3: Component Diagram
### Backend API Breakdown

```mermaid
graph TD;
    subgraph Backend API
        AuthService[Authentication Service] -->|Manages| UserDB[(User Database)]
        AttendanceService[Attendance Management] -->|Tracks| AttendanceDB[(Attendance Database)]
        ReportService[Report Generation] -->|Generates| ReportDB[(Report Database)]
    end
```

### Explanation:
- **Authentication Service:** Manages user login and registration.
- **Attendance Management:** Handles marking and verifying attendance.
- **Report Generation:** Creates attendance reports for students and teachers.

---

## C4: Code Diagram
### Class Diagram Example

```mermaid
classDiagram
    class User {
        +String id
        +String name
        +String role
    }
    
    class Attendance {
        +String studentId
        +Date date
        +Boolean status
    }
    
    class Report {
        +String teacherId
        +Date generatedDate
        +List<Attendance> attendanceRecords
    }

    User --> Attendance : "marks"
    User --> Report : "generates"
    Attendance --> Report : "is included in"
```

### Explanation:
- **User Class:** Represents students, teachers, and admins.
- **Attendance Class:** Stores attendance records.
- **Report Class:** Generates attendance reports.
