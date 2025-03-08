## Stakeholder, Functional and Non-Functional Requirements  

# Stakeholder Analysis

## 1. Students
**Role:** Primary users of the attendance management system.

### Key Concerns:
- Accurate recording of attendance
- Easy access to attendance records
- Trust in attendance accuracy
- Impact on academic progress

### Pain Points:
- Time-consuming and error-prone manual attendance marking
- Inaccessibility to real-time attendance data
- Difficulty tracking missed courses
- Risk of unfair attendance grading

### Success Metrics:
- Reduced administrative queries related to attendance
- Clear comprehension of attendance rules
- 95%+ accuracy in personal attendance records
- Real-time access to attendance data

---

## 2. Teachers and Instructors
**Role:** Tracking and monitoring student attendance.

### Key Concerns:
- Simple and fast attendance tracking
- Full reporting capabilities
- Monitoring student engagement
- Reducing paperwork

### Pain Points:
- Time-consuming manual processes
- Difficulty tracking long-term attendance patterns
- Inconsistent attendance recording methods
- Complex reporting procedures

### Success Metrics:
- 80% reduction in attendance recording time
- Instantaneous attendance report generation
- Comprehensive insights into student involvement
- Simplified record-keeping

---

## 3. University/College Administrators
**Role:** System managers and strategic planners.

### Key Concerns:
- Compliance with institutional attendance standards
- Comprehensive student performance tracking
- Resource allocation and planning
- Data-driven decision-making

### Pain Points:
- Fragmented attendance monitoring systems
- Limited insights into student participation
- Manual compilation of attendance records
- Difficulty identifying at-risk students

### Success Metrics:
- Fully digital attendance tracking
- Predictive analytics for student retention
- Instant access to institution-wide attendance data
- 60% reduction in administrative overhead

---

## 4. Parents and Guardians
**Role:** Secondary stakeholders monitoring student progress.

### Key Concerns:
- Real-time attendance visibility
- Early warning of academic concerns
- Understanding student engagement
- Communication channel with the institution

### Pain Points:
- Lack of transparency in reporting
- Limited communication on attendance
- Delayed notifications on missed classes
- Difficulty tracking long-term attendance trends

### Success Metrics:
- Instant notifications on attendance issues
- Comprehensive monthly attendance reports
- Clear visualization of academic involvement
- Reduced need for direct administration contact

---

## 5. IT Department
**Role:** Technical implementation and system maintenance.

### Key Concerns:
- Reliable and secure system design
- Scalability of the platform
- Integration with institutional systems
- Minimal technical support requirements

### Pain Points:
- High maintenance demands
- Complex legacy system integrations
- Inconsistent data management processes
- Security and data privacy challenges

### Success Metrics:
- 99.9% system uptime
- Seamless integration with existing systems
- Enhanced data protection measures
- 75% reduction in IT support requests

---

## 6. Academic Policy Makers
**Role:** Strategic planners and policy developers.

### Key Concerns:
- Data-driven policy development
- Standardized attendance monitoring
- Comprehensive student performance insights
- Institutional benchmarking

### Pain Points:
- Lack of accurate attendance data
- Difficulty identifying system issues
- Limited insights for policy adjustments
- Complex data aggregation methods

### Success Metrics:
- Comprehensive analysis of attendance trends
- Comparative institutional performance data
- Data-backed policy recommendations
- 50% faster policy development cycle

---

## 7. External Auditors
**Role:** Ensuring quality assurance and compliance.

### Key Concerns:
- Transparent and verifiable attendance records
- Compliance with educational standards
- Data integrity and authenticity
- Comprehensive reporting capabilities

### Pain Points:
- Manual record verification processes
- Inconsistent attendance documentation
- Time-consuming audit procedures
- Limited access to historical data

### Success Metrics:
- Fully digital and tamper-proof records
- Instant audit trail generation
- Simplified compliance verification
- 70% reduction in audit preparation time


# Functional Requirements

1.	User Authentication and Authorization

Requirement: To keep user data and system functions sate the system needs to have a strong login and permission system that uses role-based access control, Student, teacher and other stakeholders must have different entry rights on the system so that the users can only see data and features that are relevant to their roles. Security steps like limits on login attempts, password changes, and unique credentials must be put in place to stop people from getting in without permission.

Acceptance Criteria
User Authentication
•	Unique credentials must be used to log in by Student, teachers and administrators
Role-Based Authorization
•	Each user must have different permissions based on their roles in the system, only administrators must have full system control, include use management
Security Measures
•	After three consecutive failed login attempts a user must be locked out, unlock can be done by administrator or secured self-service recovery method after 30 minutes
Password reset Functionality 
•	User must be able to reset their password using verification method such as SMS OTP of email, the link or code for password rest must have expiration time

2.	Attendance Recording Mechanism
Requirement:  The system must be flexible, efficient and reliable to track student attendance in numerous ways, it must provide manual and automatic approaches for smooth school infrastructure integration and must capture data in a real time with timestamps to avoid manipulation.

Acceptance Criteria
Manual Attendance Input
•	A user-friendly interface must be provided to allow teachers to do manually marking of student attendance
RFID Card support
•	The RFID-card must also be supported by the system to allow student to check in and out using RFID card 


Real-Time recoding with Timestamp
•	Each entry attendance records must be logged with a accurate timestamp, any modification to attendance records should be captured.
Partial Attendance marking
•	Teacher must be allowed to mark partial attendance for late arrivals or early departures, which the system must report differentiate between full and partial attendance

3.	Comprehensive Reporting System
Requirement: The system must create through and customisable attendance reports to reveal individual and class attendance patterns, report should only be accessible by authorized users to improve data comprehension.

Acceptance Criteria
Individual Student Attendance Reports
•	The system should be able to generate attendance record for specific student, for daily, weekly, monthly and yearly, with number of present, absent and late instances
Class-Level Attendance Summaries
•	Generate attendance report for the whole class and summarize attendance trends.
Monthly and Yearly Attendance Analytics
•	The system must also generate a yearly report to analyse trend of specific period of the year

4.	Real-Time Notification System
Requirement: The system must alert stakeholders automatically about student attendance events to allow rapid communication, already defined situations should generate real-time notifications to provide prompt knowledge and intervention.

Acceptance Criteria
Automatic alerts for Low Attendance
•	Student attendance should be monitored, and alerts should be generated when attendance fall below a specified threshold.
Notification to Parents/Guardians
•	Parent should receive automated notification about student absenteeism with details including date, class details and any required follow-up actions.
Email and SMS Integration
•	Emails and SMS must also be the communication channels to send alert to stakeholders. 

5.	Attendance Analytics and Predictive Insights
Requirement: Morden data analytics must be used by the system to evaluate student attendance and academic achievement based on attendance statistics, the system should analyse trends to provide actionable insights for data driven decision making to improve student engagement and retention.

Acceptance Criteria
Correlation Analysis Between Attendance and Academic Performance
•	The system must be able to analyse historical attendance and academic performance data to identify trends and correlation which should be done for individual student, class or the whole school.
Predictive Risk Assessment for Student Dropout
•	Machine learning must be used to asset the likelihood of student dropout based on attendance patterns.
Identification of Attendance Patterns
•	The system must provide insights into factors affecting attendance, such as exam schedules, holidays or other external influences.

6.	Mobile and Multi-Platform Accessibility
Requirement: The system must be available on both computer, tablets and smartphones users, which will also support IOS and Android mobile apps and responsive online interface. 

Acceptance Criteria
Responsive Web Design
•	The system user interface and user experience must remain consistence across all devices, load fast and smooth interactions.
Native Mobile Applications (iOS/Android)
•	Dedicated mobile application for both IOS and Android must be provided, with push notification implemented for important alerts and updates. 
Offline Mode with Data Synchronization
•	Offline mode must be provided for user to be able to interact with essential features and data modification happen offline must be modified when the system is back online

7.	Academic Calendar Integration
Requirement: The tracking of attendance should be synchronized with the academic calendar of the school.

Acceptance Criteria
Calenda Import function
•	Upload calendar files manually via admin dashboard and Automatic calendar synchronization via API endpoint
Holiday and Special Event Handling
•	Automatically eliminate from attendance criteria university holidays from relevance. Support classification of days as: ordinary class days, holidays, test days, and special events.
Attendance calculation Impact
•	When calendar changes alter the overall number of class days, recalculate attendance percentages in real-time and show visible signs in the user interface when a class occurs on a holiday or special event day.

8.	Data Security and Privacy Protection
Requirement: Apply thorough data security systems following pertinent laws. via AES-256 encryption, all personally identifiable data will be encrypted both in transit via TLS 1.3 and at rest.

Acceptance Criteria
Encryption Implementation
•	Store keys in a safe key management system, encrypt database fields with personally identifiable information, rotate keys every ninety days, and offer tamper-evident audit logs using end-to-end encryption for data transport.
Regulatory Compliance
•	For GDPR, FERPA, and regional data protection requirements the solution provides data subject access requests, adjustable retention policies, data anonymization, consent management, and compliance reports.
Data Backup Protocol
•	Regular incremental and complete daily backups, geographically stored data, automated verification, point-in-time recovery assistance, and monthly restoration testing with recorded outcomes form part of the procedure.

9.	System Configuration and Customization
Requirement: Versioning, reverting to prior settings, and applying upgrades without system downtime will be possible with the configuration management interface the system will provide for approved administrators.

10.	Integration Capabilities
Requirement: The system must be compatible with past core systems, have a completely documented API with 99.5% uptime, secure authentication using OAuth 2.0 and API keys with IP limitations.


# Non-Functional Requirements

Scale and Performance
•	The system will accommodate at least 2,000 concurrent users for whom response times for any operation will not exceed 3 seconds. 
•	Even during peak usage times (8:00–9:00 AM and 12:00–1:00 PM), the system will have to provide response times below 2 seconds for 95% of all attendance record postings.
•	 Even when retrieving historical data spanning several semesters, database queries on attendance reporting must execute within five seconds.  
•	The addition of application servers to handle up to 5,000 simultaneous users during registration sessions will enable the system to horizontally scale.  
Reliability & Availability
•	The system will have 99.9% uptime on campus calendar days, hence enabling up to 8.76 hours of maximum downtime per year.
•	Single-planned maintenance only Sunday’s morning will take place and will be a minimum of 72 hours ahead of time. 
•	 System failure will be detected by failover automation systems within thirty seconds and initiate complete recovery in five minutes.  
•	The system will utilize health monitoring to notify IT personnel when availability metrics fall below 99.5% within any one-hour time frame.   
Security
•	TLS 1.3 or higher with strong cipher suites will be used for all data exchange.
•	Attendance records at rest will be AES-256 encrypted with the keys being stored in another locked key management system.  
•	With at least four different roles, student view only their records, instructor view and modify class attendance, department head view department statistics, and administrator all access, role-based access management will be utilized by the system. 
•	For administrative accounts, the system will enforce password restrictions with minimum 12 characters and complexity requirements and mandatory rotation every 90 days.  
•	The system will record timestamp, username, IP address, success or failure status in an audit trail of all authentication attempts.   
Usability and Accessibility
•	Manual testing and automated testing processes ensure that the web interface adheres to WCAG 2.1 Level AA standards. 
•	iOS 13+ and Android 10+ operating systems will be supported for the mobile app. 
•	For all main operations, the system will be keyboarding navigable and screen reader accessible.  
•	Real users of every type of role will be used to test user interfaces, thereby achieving a System Usability Scale (SUS) score of at least 75.  
•	For every operation the system will offer contextual help and tooltips.
 Maintainability and Modularity
•	Presentation, business logic, and data access levels will be distinct in the system design.
•	Attendance thresholds, notification rules, grading policies and all configuration parameters will be externalized in a configuration management system accessible to managers without requiring code changes.  
•	For each part of business logic, the codebase should maintain at least 80% test coverage.  
•	Code documentation will follow established guidelines such as extensive API documentation.  
•	Dependency injecting will be utilized by the system to allow component testing and substitutability.
Logging and Audit
•	Every system event will be recorded in a uniform format of IP address, date/time, user ID, action type, impacted record IDs.
•	With threshold-controllable alerts, the logging facility will support several levels of severity such as INFO, Warning, ERROR, CRITICAL.
•	With automatic archiving options, logs will be kept in tamper-evident format and held for minimum one year.
•	For basic compliance needs such as attendance records, access attempts—the system will offer pre-defined audit reports.
•	Administrative log access will be two-factor authenticated and will alert security staff.

Integration & Interoperability
•	Restful APIs with OpenAPI 3.0 documentation for all fundamental operations will be showcased by the system.
•	OpenID Connect for single sign-on integration with university identity providers and SAML 2.0 will be facilitated by the system.
•	Integration with current student information system will be done with real-time synchronizing with a maximum latency of 15 minutes.
•	 The system will offer webhooks for real-time notifications of attendance events to third-party systems.  
•	All APIs will employ rate limiting to avoid abuse via client application-configurable limits.  

Recovery & Backup of Data
•	The system will have incremental backups every six hours, at night during off-peak it will have full backups.
•	The Recovery Time Objective shall be less than 1 hour for critical information.
•	Recovery Point Objective shall not exceed 1 hour's data loss under any failure condition. 
•	Backups will be preserved in geographically diverse locations with at least one being in another region than the main system. 
•	 Monthly tests of backup and recovery procedures shall give documented outputs.
Compliance and Legal Requirements:
•	For complying with data residency requirements, geographical separation of data will be retained in the system.  
•	Personal data will be anonymised whenever identification of the individuals is not a requirement for reporting and analytics.
•	Data retention will be data-type configurable with an automatic cleanup of data expired on date. 
•	There will be provision of data export facility within five business days for meeting subject access requests. 
•	Detailed records of every data access shall be stored for compliance reporting reasons.
