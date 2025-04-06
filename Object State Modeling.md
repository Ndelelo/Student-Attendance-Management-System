# Object State Modeling with State Transition Diagrams

## 1. Attendance Record

![Attendance Record State Diagram](mermaid-diagram-Attendance.png)

```mermaid
stateDiagram-v2
    [*] --> Initialized : Initialize()
    Initialized --> Marked : MarkAttendance()
    Marked --> Verified : VerifyAttendance()
