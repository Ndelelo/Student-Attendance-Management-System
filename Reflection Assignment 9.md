# Reflection: Designing the Domain Model and Class Diagram

The process of making the domain model and class diagram for the **Student Attendance Management System** was both exciting and demanding. It required a deep understanding of object-oriented design principles, the unique challenges of academic environments, and finding the right balance between abstraction and detail.

---

## 1. Domain Model and Class Diagram Design Challenges

- **Abstraction Level:**  
  It was challenging to choose what to model. While modeling real-world details like student year levels, vacations, and course credits was tempting, I had to stay focused on core **attendance functionality** rather than building a full academic administration system.

- **Entity Relationships:**  
  Defining relationships, especially the **many-to-many** link between Students and Courses, was complex. I realized that attendance records should not be embedded but instead modeled as a separate `AttendanceRecord` entity that links a Student, Course, and Date. This helped preserve clean, object-oriented design.

- **Method Design (Responsibilities):**  
  Determining what actions each class should handle (e.g., recording vs. viewing attendance) helped me avoid violating the **Single Responsibility Principle**. Delegating responsibilities wisely improved cohesion.

---

## 2. Alignment with Previous Assignments (Use Cases, State Diagrams, Requirements)

- **Use Cases:**  
  Use cases like *“Mark Attendance”* influenced my class interactions. The flow of an Instructor selecting a Course, then a Student, and recording attendance shaped method logic and associations.

- **State Diagrams:**  
  Modeling the lifecycle of `AttendanceRecord` (e.g., Created → Updated → Finalized) highlighted the need for update methods and validation logic.

- **Requirements:**  
  System requirements emphasized **security and access control**, validating design decisions like limiting attendance editing to assigned instructors.

---

## 3. Trade-Offs and Design Decisions

- **Avoiding Inheritance for Roles:**  
  Although creating a `User` superclass with `Student` and `Teacher` subclasses seemed logical, their limited shared attributes made this impractical. I opted for **independent entities** to reduce tight coupling.

- **Composition vs. Aggregation:**  
  - Used **composition** between `Student` and `AttendanceRecord`—since attendance makes no sense without a student.
  - Used **aggregation** between `Course` and `Schedule`—allowing schedule reuse and independent updates.

---

## 4. Lessons Learned About Object-Oriented Design

This exercise improved my grasp of key OOP concepts:

- ✅ **Cohesion and Responsibility:**  
  Every class must serve a single, clear purpose.

- ✅ **Encapsulation:**  
  Grouping attributes and behaviors logically supports maintainability.

- ✅ **Loose Coupling:**  
  Design should support changes in one area without affecting others.

- ✅ **Reusability & Extensibility:**  
  Flexible design eases future updates and integration.

> 📌 **Final Insight:**  
> Modeling is not about capturing *everything* - it's about capturing the *right things*. A clear, clean domain model simplifies everything from database design to implementation and testing.

