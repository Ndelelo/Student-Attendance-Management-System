# Reflection

---

## 1. Challenges in Choosing Granularity for States and Actions

Finding the appropriate level of detail is a major challenge when designing Activity Diagrams (ADs) and State Transition Diagrams (STDs).

### Key Challenges:
- **Too Elaborate**: Diagrams become cluttered and hard to interpret, leading to maintenance issues.
- **Too Abstract**: Critical system behavior may be overlooked, reducing accuracy.

### Example:
- **Modeling Student State**:  
  Should there be just one "Enrolled" state, or should we distinguish between "Registered", "Verified", and "Active"?
- **Attendance Marking**:  
  Should every teacher action be collapsed into a single "Mark Attendance" node, or broken down into multiple steps?

### Best Practices:
- Use **high-level states** for clarity.
- Employ **nested states** or **sub-diagrams** when more detail is necessary.
- Model from the **user’s perspective**—developers might prefer technical details, but simplicity aids usability.

---

## 2. Aligning Agile User Stories with Diagrams

Agile development focuses on **user-centric**, incremental builds, while UML diagrams often attempt to model the entire system upfront.

### Challenges:
- **Rigid structure** of diagrams doesn't always align with Agile's **flexibility**.
- **Traceability** becomes complex when one user story affects multiple diagrams or flows.

### Example:
- **User Story**: "As a Teacher, I want to mark attendance for my class."
  - **Activity Diagram**: Login → Select Class → Mark Present/Absent → Submit
  - **State Diagram**:  
    - *Student*: Present ↔ Absent  
    - *System*: Draft → Submitted
- Agile iteration may later add "Bulk Marking" or "AI-based Attendance", requiring diagram updates.

### Perfect Practice:
- Use **lightweight diagrams** that are easy to evolve with Agile sprints.
- Prefer **modular diagrams** over monolithic ones.
- Focus on **core workflows** first—perfect coverage can come later.

---

## 3. Comparing State Diagrams vs. Activity Diagrams

| **Aspect**       | **State Transition Diagram (STD)**                                | **Activity Diagram (AD)**                                  |
|------------------|--------------------------------------------------------------------|-------------------------------------------------------------|
| **Focus**        | Object behavior over time                                          | Process and workflow execution                              |
| **Use Case**     | Lifecycle of objects (e.g., a student from registration to grad)   | Task sequences (e.g., a teacher marking attendance)         |
| **Example**      | Student: Unregistered → Registered → Verified → Graduated         | Login → Select Class → Mark → Submit                        |
| **Best for**     | Modeling constraints (e.g., avoid duplicate attendance)            | Understanding user flow and decision points                 |
| **Challenges**   | Choosing meaningful states, concurrency                            | Managing complexity when multiple actors are involved       |

---

## Lessons Learned: Reflection on System Modeling

### Granularity in Diagrams:
- Balance between **detail and abstraction** is key.
- Use **nested states** where deeper clarity is needed.
- Always model with the **end user** in mind.

### Agile Compatibility:
- Traditional UML may be out of sync with Agile flow.
- Diagrams can become obsolete as user stories change.
- Use **modular, updatable, lightweight diagrams** to support agile iterations.

### Combining Diagram Types:
- **STDs** model system rules and object states.
- **ADs** highlight user interactions and task flows.
- Combining both gives a **complete view** of the system from both behavioral and functional perspectives.
