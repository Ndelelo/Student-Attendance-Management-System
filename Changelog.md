# Changelog

All notable changes to this project are documented in this file.


### Added
- Implemented all six creational design patterns:
  - Singleton
  - Factory Method
  - Abstract Factory
  - Builder
  - Prototype
  - Object Pool

### Fixed
- Fix #15: Made Singleton thread-safe for multithreaded use
- Corrected return values in Abstract Factory for better clarity
- Improved error handling in Builder and Object Pool patterns

### Changed
- Refactored Factory pattern to be more modular
- Enhanced Prototype pattern with deep copy logic
- Optimized Object Pool initialization and resource reuse

### Tests
- Achieved 98% test coverage in `test_creational_patterns.py`
- Added test cases for edge cases and exception handling in `main.py`

### Documentation
- Created detailed docstrings and inline comments for each pattern
- Linked relevant issues to commits (Improvement: Increase test coverage for main.py)
- Added this `CHANGELOG.md` for tracking project changes

---