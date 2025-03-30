# Kanban Board Overview

![Kanban Board](KanbanBoard.jpg)


![Kanban Board - Testing](Kanban.jpg)

### **Testing Column**

- **Testing** guarantees in Agile development that features satisfy quality criteria before they are labelled as Done.
- Including a testing column enables an organized review and feedback loop; quality checks prior to release; bug or performance issues identification.

#### **How Does Automation Work**
- After a **Pull Request (PR)** is accepted, move to "Testing".
- After testing is finished and integrated, move to "Done".

---

### **Blocked Column**

The **Blocked Column** was added to the Kanban board for managing task dependencies that prevent further progress.

#### **Blocking Stage**
- A Blocked column helps identify dependencies and stops flow congestion in your system.
- This stage is helpful when outside dependencies prevent a job from starting.
- Stopping progress calls for a waiting time, and a major issue (such as a bug or delayed approval) calls for this as well.

#### **How Does Automation Work**
- Change to Blocked when a **PR** or **issue** gains a **blocked label**.
- When the label is taken off, return to **In Progress**.

---