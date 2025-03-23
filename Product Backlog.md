# Product Backlog

**Prioritized product backlog using MoSCoW prioritization and effort estimates:**

## 1. Backlog Items

| Story ID | User Story | Priority (MoSCoW) | Effort Estimate (1-5) | Dependencies |
|----------|------------|-------------------|----------------------|--------------|
| US001 | As a student, I want to log in securely so that I can access my data safely. | Must-have | 3 | None |
| US002 | As a teacher, I want to mark student attendance manually so that I can keep records for each session. | Must-have | 2 | US001 |
| US003 | As a student, I want to check in using an RFID card so that my attendance is recorded automatically. | Must-have | 4 | US001 |
| US004 | As an admin, I want to generate attendance reports so that I can analyze student attendance trends. | Must-have | 3 | US002, US003 |
| US005 | As a parent, I want to receive notifications when my child is absent so that I can follow up on attendance issues. | Must-have | 3 | US004 |
| US006 | As a school administrator, I want attendance reports to show patterns so that I can make data-driven decisions. | Should-have | 4 | US004 |
| US007 | As a student, I want to apply for leave online so that I can request absences conveniently. | Should-have | 2 | US001 |
| US008 | As a teacher, I want to approve or reject leave requests so that I can manage class attendance records accurately. | Should-have | 3 | US007 |
| US009 | As a student, I want to access my attendance records so that I can track my presence in class. | Could-have | 2 | US002 |
| US010 | As a system administrator, I want all student data to be encrypted with AES-256 so that security compliance is maintained. | Must-have | 5 | None |
| US011 | As an admin, I want to configure attendance policies so that I can set rules for different institutions. | Could-have | 3 | US004 |
| US012 | As a student, I want to access the system on my phone so that I can check my attendance status on the go. | Should-have | 4 | US009 |

---

## 2. Justification for Prioritization

1. **Must-Have** stories are essential for system functionality and security.  
   - Without authentication (**US001**), the system cannot operate.  
   - Attendance tracking (**US002, US003**) and reporting (**US004**) are core features.  
   - Security (**US010**) ensures compliance.  

2. **Should-Have** stories improve usability but are not immediately critical.  
   - Features like leave requests (**US007, US008**) and advanced analytics (**US006**) enhance user experience but do not block core operations.  

3. **Could-Have** stories are nice additions but can be deferred.  
   - Mobile access (**US012**) and attendance history (**US009**) add convenience but do not impact the system’s main functionality.  

4. **Won’t-Have** stories (if applicable) are either out of scope or unnecessary for the current release.  
