# Student Attendance Management System

## Justification

### Language Choice: Python

Python was selected for developing the **Student Attendance Management System** because of its:

- **Ease of use and readability** – ideal for implementing and understanding design patterns.
- **Object-oriented structure** – aligns well with the system’s entity-based model (e.g., `Student`, `Teacher`, `Course`).
- **Quick prototyping ability** – perfect for building and demonstrating core system logic with minimal setup.

---

###  Design Decisions: Creational Patterns

To ensure clean, maintainable, and scalable architecture, all six **creational design patterns** were implemented with direct relevance to the Student Management Attendance System:

| Pattern             | Real-World Application                                     | Reason for Use |
|---------------------|------------------------------------------------------------|----------------|
| **Singleton**        | `Logger` - Used to log all attendance actions across the system. | Guarantees a single shared instance of logging, avoiding duplicates or inconsistencies. |
| **Factory Method**   | `NotificationFactory` - Sends email/SMS alerts when attendance is marked. | Abstracts notification creation, allowing easy extension (e.g., add push notifications). |
| **Abstract Factory** | `GUIFactory` - Produces themed UI components (e.g., buttons for light/dark mode). | Prepares for future GUI support with consistent UI generation logic. |
| **Builder**          | `ReportBuilder` - Generates detailed attendance reports for teachers/admins. | Handles step-by-step report construction, supporting flexible formatting and customization. |
| **Prototype**        | `CourseTemplate` - Allows quick duplication of existing course structures. | Enables efficient reuse of course definitions with minimal manual setup. |
| **Object Pool**      | `ConnectionPool` - Manages reusable DB connections (simulated). | Demonstrates how resource pooling would reduce overhead in real-world database scenarios. |

