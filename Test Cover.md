##  Test Coverage

| Test Case                                 | Status |
|------------------------------------------|--------|
| test_abstract_factory_dark_button         | ✅ ok  |
| test_abstract_factory_light_button        | ✅ ok  |
| test_builder_report                       | ✅ ok  |
| test_factory_email_notification           | ✅ ok  |
| test_factory_invalid_method               | ✅ ok  |
| test_factory_sms_notification             | ✅ ok  |
| test_object_pool_connection_reuse         | ✅ ok  |
| test_object_pool_exhaustion               | ✅ ok  |
| test_prototype_course_clone               | ✅ ok  |
| test_singleton_logger                     | ✅ ok  |

## ✅ Test Summary

- ✅ **10 tests** were discovered and run  
- ✅ **Every creational pattern was covered:**
  - **Singleton:** Logger  
  - **Factory Method:** Email & SMS notification creation  
  - **Abstract Factory:** UI themes  
  - **Builder:** Attendance report  
  - **Prototype:** Course template cloning  
  - **Object Pool:** Simulated DB connection reuse and exhaustion  

---

## 📊 Coverage Breakdown

| File                       | Coverage | Notes                                                                 |
|----------------------------|----------|------------------------------------------------------------------------|
| `main.py`                  | 72%      | Some logic still untested — could be edge cases, error handling, or branches. |
| `test_creational_patterns.py` | 98%      | Excellent — nearly all test code is executed.                          |
| **Total**                  | **81%**  | Above average.                                |
