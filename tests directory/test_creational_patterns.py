import unittest
from main import (
    Logger, NotificationFactory, EmailNotification, SMSNotification,
    LightThemeFactory, DarkThemeFactory, ReportBuilder,
    CourseTemplate, ConnectionPool
)

class TestCreationalPatterns(unittest.TestCase):

    def test_singleton_logger(self):
        logger1 = Logger()
        logger2 = Logger()
        self.assertIs(logger1, logger2)

    def test_factory_email_notification(self):
        notifier = NotificationFactory.create_notification("email")
        self.assertIsInstance(notifier, EmailNotification)

    def test_factory_sms_notification(self):
        notifier = NotificationFactory.create_notification("sms")
        self.assertIsInstance(notifier, SMSNotification)

    def test_factory_invalid_method(self):
        with self.assertRaises(ValueError):
            NotificationFactory.create_notification("fax")

    def test_abstract_factory_light_button(self):
        factory = LightThemeFactory()
        button = factory.create_button()
        self.assertEqual(button.__class__.__name__, "LightButton")

    def test_abstract_factory_dark_button(self):
        factory = DarkThemeFactory()
        button = factory.create_button()
        self.assertEqual(button.__class__.__name__, "DarkButton")

    def test_builder_report(self):
        builder = ReportBuilder()
        report = (builder.add_header("Test Report")
                        .add_attendance_record("John", "Present")
                        .add_footer()
                        .build())
        self.assertIn("==== Test Report ====", report.display())
        self.assertIn("John - Present", report.display())
        self.assertIn("==== End of Report ====", report.display())

    def test_prototype_course_clone(self):
        original = CourseTemplate("Math", "Dr. Mukwevho")
        original.add_material("Chapter 1")
        clone = original.clone()
        self.assertNotEqual(id(original), id(clone))
        self.assertEqual(clone.title, "Math")
        self.assertEqual(clone.teacher, "Dr. Mukwevho")
        self.assertIn("Chapter 1", clone.materials)

    def test_object_pool_connection_reuse(self):
        pool = ConnectionPool(2)
        conn1 = pool.get()
        conn2 = pool.get()
        self.assertIsNotNone(conn1)
        self.assertIsNotNone(conn2)
        pool.release(conn1)
        pool.release(conn2)
        conn3 = pool.get()
        self.assertIsNotNone(conn3)

    def test_object_pool_exhaustion(self):
        pool = ConnectionPool(1)
        conn1 = pool.get()
        conn2 = pool.get()  # Should return None as pool is empty
        self.assertIsNotNone(conn1)
        self.assertIsNone(conn2)

if __name__ == '__main__':
    unittest.main()
