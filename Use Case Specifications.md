## Use Case Specifications

### **Use Case: Mark Attendance**
**Actor:** Teacher  
**Precondition:**  
- Teacher is logged into the system.  
- The class session is scheduled, and the list of students is available.  
- The system is operational, and the student attendance records are accessible.  
**Postcondition:**  
- Attendance is recorded successfully for each student.  
- Attendance data is saved in the system for future reference and reporting.  
**Basic Flow:**  
1. The teacher logs into the system.  
2. The teacher selects the class session for which they need to mark attendance.  
3. The system displays the list of registered students for that session.  
4. The teacher marks each student's attendance as present or absent.  
5. The teacher submits the attendance record.  
6. The system saves the attendance data and confirms the successful recording of attendance.  

---

### **Use Case: View Attendance Record**
**Actor:** Parent/Teacher  
**Precondition:**  
- The user is logged into the system.  
- The user has the necessary permissions to view attendance records.  
**Postcondition:**  
- Attendance history is displayed for the selected student.  
**Basic Flow:**  
1. The user logs into the system.  
2. The user navigates to the Attendance section.  
3. The system displays a list of available records (student, class, or date range).  
4. The user selects the desired student or date range.  
5. The system displays the detailed attendance record.  
6. The user can view or print the attendance history.  

---

### **Use Case: Apply for Leave**
**Actor:** Student  
**Precondition:**  
- The student or parent is logged into the system.  
- The student is enrolled in the class for which they wish to apply for leave.  
- The leave request has a valid reason such as illness or personal matters.  
**Postcondition:**  
- The leave request is successfully submitted for approval.  
- The system updates the student's leave status to "pending" until reviewed.  
**Basic Flow:**  
1. The student or parent logs into the system.  
2. The student navigates to the "Leave Request" section.  
3. The student selects the class and dates for the leave.  
4. The student enters a reason for the leave.  
5. The student submits the request.  
6. The system stores the leave request and notifies the teacher or admin for approval.  

---

### **Use Case: Approve Leave Requests**
**Actor:** Teacher  
**Precondition:**  
- The teacher or admin is logged into the system.  
- There is at least one pending leave request for review.  
- The teacher or admin has the necessary permissions to approve or deny leave requests.  
**Postcondition:**  
- The leave request is either approved or denied.  
- The student’s attendance status is updated accordingly.  
**Basic Flow:**  
1. The teacher or admin logs into the system.  
2. The teacher navigates to the "Leave Requests" section.  
3. The teacher reviews the list of pending requests.  
4. The teacher decides whether to approve or deny the leave.  
5. The system updates the leave status in the student’s attendance record.  

---

### **Use Case: Generate Attendance Reports**
**Actor:** Administrator  
**Precondition:**  
- The admin is logged into the system.  
- The system has stored sufficient attendance data.  
- The admin has the required permissions to generate reports.  
**Postcondition:**  
- The report is generated and saved in the system.  
- The report can be downloaded or viewed by the admin.  
**Basic Flow:**  
1. The admin logs into the system.  
2. The admin navigates to the "Reports" section.  
3. The admin selects the report type and filters either by date range, class, or student.  
4. The system generates the report based on the selected criteria.  
5. The admin reviews the report or exports it for further use.  

---

### **Use Case: Backup and Restore Data**
**Actor:** IT Department  
**Precondition:**  
- The IT department has the necessary permissions to access the system’s data.  
- The system is operational, and data is available for backup.  
**Postcondition:**  
- The attendance data is backed up and securely stored.  
- In the case of data corruption or loss, the data can be restored from the backup.  
**Basic Flow:**  
1. The IT department logs into the system.  
2. The IT department navigates to the "Backup" section.  
3. The IT department initiates the backup process.  
4. The system creates a backup of the attendance records and confirms process completion.  

---

### **Use Case: Ensure Compliance**
**Actor:** External Auditors  
**Precondition:**  
- The external auditor has logged into the system.  
- The system contains a sufficient history of attendance records for review.  
- The auditor has permission to access and review attendance data.  
**Postcondition:**  
- The auditor verifies that the attendance records are accurate and compliant with policies and regulations.  
- If discrepancies are found, the auditor may raise issues for further review or correction.  
**Basic Flow:**  
1. The auditor logs into the system.  
2. The auditor navigates to the "Compliance" section.  
3. The system displays all necessary records and compliance checks.  
4. The auditor reviews the attendance records for the selected period and student group.  
5. The auditor cross-checks the attendance records against institutional and regulatory policies.  
6. If compliant, the auditor marks the audit as successful.  
7. If non-compliant, the auditor generates a report highlighting discrepancies and potential issues.  

---

### **Use Case: Define Attendance Policies**
**Actor:** Academic Policymakers  
**Precondition:**  
- The academic policymaker is logged into the system with the appropriate permissions to modify attendance policies.  
- The system is operational and capable of saving and applying the policies.  
**Postcondition:**  
- The new or modified attendance policies are saved in the system.  
- The system updates any relevant processes, such as notifying students or applying restrictions based on the new policies.  
**Basic Flow:**  
1. The policymaker logs into the system.  
2. The policymaker navigates to the "Attendance Policies" section.  
3. The system displays the current policies.  
4. The policymaker modifies or defines new policies.  
5. The policymaker saves the new or modified policy.  
6. The system applies the policy across all relevant student and teacher records.  
