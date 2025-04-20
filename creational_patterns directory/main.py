from abc import ABC, abstractmethod
import copy

# 1. Singleton - Logger
class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    def log(self, message):
        print(f"[LOG]: {message}")


# 2. Factory Method - Notification
class Notification(ABC):
    @abstractmethod
    def send(self, message): pass

class EmailNotification(Notification):
    def send(self, message):
        print(f"[EMAIL] {message}")

class SMSNotification(Notification):
    def send(self, message):
        print(f"[SMS] {message}")

class NotificationFactory:
    @staticmethod
    def create_notification(method):
        if method == "email":
            return EmailNotification()
        elif method == "sms":
            return SMSNotification()
        else:
            raise ValueError("Unsupported method")


# 3. Abstract Factory - GUI Components
class Button(ABC):
    @abstractmethod
    def draw(self): pass

class LightButton(Button):
    def draw(self): print("Drawing Light Button")

class DarkButton(Button):
    def draw(self): print("Drawing Dark Button")

class GUIFactory(ABC):
    @abstractmethod
    def create_button(self): pass

class LightThemeFactory(GUIFactory):
    def create_button(self): return LightButton()

class DarkThemeFactory(GUIFactory):
    def create_button(self): return DarkButton()


# 4. Builder - Attendance Report
class Report:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def display(self):
        return "\n".join(self.parts)

class ReportBuilder:
    def __init__(self):
        self.report = Report()

    def add_header(self, title):
        self.report.add(f"==== {title} ====")
        return self

    def add_attendance_record(self, name, status):
        self.report.add(f"{name} - {status}")
        return self

    def add_footer(self):
        self.report.add("==== End of Report ====")
        return self

    def build(self):
        return self.report


# 5. Prototype - Course Template
class CourseTemplate:
    def __init__(self, title, teacher):
        self.title = title
        self.teacher = teacher
        self.materials = []

    def add_material(self, material):
        self.materials.append(material)

    def clone(self):
        return copy.deepcopy(self)


# 6. Object Pool - DB Connections
class DBConnection:
    def __init__(self, id):
        self.id = id

    def query(self, sql):
        print(f"[DB {self.id}] Executing: {sql}")

class ConnectionPool:
    def __init__(self, size):
        self.pool = [DBConnection(i) for i in range(size)]

    def get(self):
        return self.pool.pop() if self.pool else None

    def release(self, conn):
        self.pool.append(conn)


# CLI Demo
if __name__ == "__main__":
    print("--- Singleton Logger ---")
    Logger().log("System Initialized")

    print("\n--- Factory Method (Notification) ---")
    notifier = NotificationFactory.create_notification("email")
    notifier.send("Welcome to Attendance System")

    print("\n--- Abstract Factory (GUI Button) ---")
    theme = LightThemeFactory()
    btn = theme.create_button()
    btn.draw()

    print("\n--- Builder (Attendance Report) ---")
    builder = ReportBuilder().add_header("Attendance Report")
    builder.add_attendance_record("Alice", "Present").add_attendance_record("Bob", "Absent")
    report = builder.add_footer().build()
    print(report.display())

    print("\n--- Prototype (Course Template) ---")
    course = CourseTemplate("Intro to Python", "Dr. A")
    course.add_material("Week 1")
    cloned = course.clone()
    cloned.title = "Advanced Python"
    print(f"Original: {course.title}, Clone: {cloned.title}")

    print("\n--- Object Pool (DB Connections) ---")
    pool = ConnectionPool(2)
    conn = pool.get()
    if conn:
        conn.query("SELECT * FROM attendance")
        pool.release(conn)
    else:
        print("No connections available")
