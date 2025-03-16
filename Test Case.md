# Test Case Development  

## Functional Requirements  

### Test Case Table  

| **Test Case ID** | **Requirement ID** | **Description** | **Steps** | **Expected Result** | **Actual Result** | **Status (Pass/Fail)** |
|---------------|---------------|--------------------|--------|-------------------|----------------|----------------|
| TC-001 | FR-001 | User Authentication | 1. Enter valid credentials. 2. Click "Login". | User should be successfully logged in based on role. | Successfully logged | Pass |
| TC-002 | FR-001 | Login Lockout after 3 Failed Attempts | 1. Enter incorrect credentials 3 times. 2. Try to log in again. | User should be locked out and prompted with recovery options. | Unsuccessfully locked out | Fail |
| TC-003 | FR-002 | Manual Attendance Input | 1. Teacher enters student attendance manually. 2. Click "Submit". | Attendance should be successfully marked with timestamp and saved. | Successfully submitted | Pass |
| TC-004 | FR-002 | RFID Card Support for Attendance | 1. Student scans RFID card. 2. Check attendance status. | Attendance should be automatically marked and timestamped. | Not yet active | Fail |
| TC-005 | FR-003 | Generate Individual Student Attendance Report | 1. Teacher/admin selects a student. 2. Generate report for daily, weekly, monthly. | Report is generated showing presence, absences, and late entries. | Can be able to select student | Fail |
| TC-006 | FR-004 | Automatic Alerts for Low Attendance | 1. Student attendance falls below threshold. 2. Check alert. | Alert should be automatically triggered and sent via email/SMS. | Successfully generate Alert | Pass |
| TC-007 | FR-006 | Generate Monthly Attendance Analytics | 1. Admin generates monthly attendance report. 2. Analyze trends. | Report should show monthly attendance trends with statistical analysis. | Able to generate report | Pass |
| TC-008 | FR-007 | Mobile Accessibility | 1. Open system on mobile app (iOS/Android). 2. Perform actions like attendance marking. | UI should be responsive, and functions should work smoothly on mobile. | Not yet implemented | Fail |



## Data Backup and Recovery  

### Test Case Table  

| **Test Case ID** | **Requirement ID** | **Description** | **Steps** | **Expected Result** | **Actual Result** | **Status (Pass/Fail)** |
|---------------|---------------|--------------------|--------|-------------------|----------------|----------------|
| TC-013 | FR-009 | Automatic Data Backup | 1. Schedule automatic backups. 2. Verify backup completion after the scheduled time. | Backup should complete successfully and be verified for integrity. | Can’t be tested now | N/A |
| TC-014 | FR-009 | Data Recovery Process | 1. Simulate data loss. 2. Initiate recovery process using backup data. | Data should be restored to the state it was at the time of backup. | Can’t be tested now | N/A |



## Integration with External Systems  

### Test Case Table  

| **Test Case ID** | **Requirement ID** | **Description** | **Steps** | **Expected Result** | **Actual Result** | **Status (Pass/Fail)** |
|---------------|---------------|--------------------|--------|-------------------|----------------|----------------|
| TC-015 | FR-010 | API Integration with LMS | 1. Initiate integration between the attendance system and LMS. 2. Verify synchronization of attendance data. | Attendance data should be synchronized between the systems without discrepancies. | It can relate to other system now | N/A |
| TC-016 | FR-010 | Data Synchronization with SIS | 1. Update attendance in the system. 2. Verify that the updated data appears in the SIS. | Attendance data should automatically update and synchronize in the SIS. | It can relate to other system for now | N/A |

---

## Non-Functional Requirements  

### Performance Testing  

| **Test Case ID** | **Requirement ID** | **Description** | **Steps** | **Expected Result** | **Actual Result** | **Status (Pass/Fail)** |
|---------------|---------------|--------------------|--------|-------------------|----------------|----------------|
| TC-009 | NFR-001 | Load Testing with 1000 Concurrent Users | 1. Simulate 1000 concurrent users. 2. Perform typical actions (e.g., logging in, attendance input). | System should perform all actions within 3 seconds per operation. | Unable to perform the task | Fail |
| TC-010 | NFR-001 | Peak Usage Performance | 1. Simulate peak usage between 8:00–9:00 AM. 2. Record system response time for 95% of attendance records. | Response time for 95% of operations should be ≤ 2 seconds. | Test can be done for now | Fail |



### Security Testing  

| **Test Case ID** | **Requirement ID** | **Description** | **Steps** | **Expected Result** | **Actual Result** | **Status (Pass/Fail)** |
|---------------|---------------|--------------------|--------|-------------------|----------------|----------------|
| TC-011 | NFR-002 | Test TLS 1.3 Encryption | 1. Simulate data exchange between client and server. 2. Inspect data transmission. | TLS 1.3 encryption with strong cipher suites should be used. | Cannot be done on system current state | Fail |
| TC-012 | NFR-002 | Role-Based Access Control | 1. Log in as student, teacher, admin with different credentials. 2. Try accessing restricted data. | Each user role should only have access to relevant data based on permissions. | Student successfully logged in and unable to access restricted data | Pass |






-----

# Reflection

Translating requirements into tests for a **Student Attendance Management System** was challenging due to several factors. Some key challenges include:

## 1. Features Yet to be Implemented  
Multiple test cases, such as **RFID card support, mobile accessibility, and API integration**, either failed or could not be assessed due to the features not being active or implemented at this time.  

**Challenge:** The alignment of test cases with the development progress necessitates regular updates.  

## 2. Insufficient Requirements  
Several test cases, such as **TC-002 related to login lockout**, did not pass because the requirements regarding the expected behavior were not clearly defined. For instance, the system failed to lock the user out as intended.  

**Challenge:** It is essential for requirements to outline specific expected behaviors to prevent inconsistencies in test outcomes.  

## 3. Limitations of Performance Testing  
The **load testing (TC-009) and peak usage performance (TC-010)** failed as the system was unable to manage a significant volume of concurrent users effectively.  

**Challenge:** The evaluation of performance necessitates the use of simulation tools and infrastructure that can accommodate extensive testing scenarios.  

## 4. Limitations in Security Testing  
The **testing for TLS 1.3 encryption (TC-011)** was not able to be conducted because of limitations within the system.  

**Challenge:** The process of security testing necessitates the use of specialized tools and configurations, which may not be accessible in the initial stages of development.  

## 5. Challenges in Integration  
The testing of **API integration with Learning Management Systems (LMS) and Student Information Systems (SIS) (TC-015 & TC-016)** was not possible due to the incomplete status of the integration.  

**Challenge:** Coordination with third-party systems is essential due to external system dependencies and the need for data synchronization.  

## 6. Issues Related to Data Backup and Recovery Testing  
The execution of test cases for **automatic backup and data recovery (TC-013 & TC-014)** was not possible.  

**Challenge:** Simulating data loss and assessing the effectiveness of recovery processes necessitates a carefully managed test environment.  

## 7. User Experience and Mobile Compatibility  
The **mobile accessibility testing (TC-008)** did not pass because the system has not been configured for mobile usage.  

**Challenge:** Achieving cross-platform usability necessitates thorough **UI/UX testing** across various devices.  

