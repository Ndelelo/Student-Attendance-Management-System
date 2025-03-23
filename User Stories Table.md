
# Student Attendance Management System - User Stories


## 1. User Story Table

| Story ID | User Story | Acceptance Criteria | Priority |
|----------|------------|---------------------|----------|
| US001 | As a student, I want to log in securely so that I can access my data safely. | Users must authenticate using unique credentials, with role-based access control. After three failed attempts, the account is locked. | High |
| US002 | As a teacher, I want to mark student attendance manually so that I can keep records for each session. | A user-friendly interface must allow teachers to mark attendance. The system saves records in real time. | High |
| US003 | As a student, I want to check in using an RFID card so that my attendance is recorded automatically. | The system must support RFID-based check-in and record timestamps. | High |
| US004 | As an admin, I want to generate attendance reports so that I can analyse student attendance trends. | Reports must be available for individual students and whole classes with various timeframes (daily, weekly, monthly, yearly). | High |
| US005 | As a parent, I want to receive notifications when my child is absent so that I can follow up on attendance issues. | Parents receive automated notifications via email/SMS when a student is absent. | High |
| US006 | As a school administrator, I want attendance reports to show patterns so that I can make data-driven decisions. | Reports should analyse trends, showing correlations between attendance and performance. | Medium |
| US007 | As a student, I want to apply for leave online so that I can request absences conveniently. | The system must allow students to submit leave requests with reasons, and update status upon approval. | Medium |
| US008 | As a teacher, I want to approve or reject leave requests so that I can manage class attendance records accurately. | Teachers must be able to approve/reject requests, updating the student's attendance status accordingly. | Medium |
| US009 | As a student, I want to access my attendance records so that I can track my presence in class. | The system must display a student's attendance history in an easy-to-read format. | Low |
| US010 | As a system administrator, I want all student data to be encrypted with AES-256 so that security compliance is maintained. | All personal data must be encrypted in transit (TLS 1.3) and at rest (AES-256). | High |
| US011 | As an admin, I want to configure attendance policies so that I can set rules for different institutions. | Admins must be able to set attendance thresholds, auto-excuse rules, and class weightage. | Medium |
| US012 | As a student, I want to access the system on my phone so that I can check my attendance status on the go. | The system must provide a responsive web design and native mobile apps for iOS and Android. | High |
---
