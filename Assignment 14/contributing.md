# Contributing to Student Attendance System

Thank you for considering contributing to the Student Attendance System! This document outlines the process for contributing to this project and helps you get started as a contributor.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation Instructions](#installation-instructions)
- [Development Workflow](#development-workflow)
- [Coding Standards](#coding-standards)
- [Testing Guidelines](#testing-guidelines)
- [Issue Selection Process](#issue-selection-process)
- [Pull Request Process](#pull-request-process)
- [Communication](#communication)

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package manager)
- Git
- A code editor (VS Code, PyCharm, etc.)
- MySQL or PostgreSQL (depending on project configuration)

## Installation Instructions

1. **Fork the repository**
   
   Start by forking the repository to your GitHub account.

2. **Clone your fork**
   ```bash
   git clone https://github.com/Ndelelo/Student-Attendance-Management-System.git
   cd student-attendance-system
   ```

3. **Set up a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # Development dependencies
   ```

5. **Set up the database**
   ```bash
   # Configure your database connection in .env file (use .env.example as template)
   cp .env.example .env
   
   # Run migrations
   python manage.py migrate
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

## Development Workflow

1. **Create a new branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Write code that implements the feature or fixes the bug
   - Add or update tests as necessary
   - Update documentation if needed

3. **Commit your changes**
   ```bash
   git add .
   git commit -m "Description of changes"
   ```

4. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

5. **Create a Pull Request**
   - Go to the original repository
   - Click "New Pull Request"
   - Select your fork and branch
   - Fill out the PR template with details of your changes

## Coding Standards

We follow PEP 8 style guidelines for Python code. Additionally:

- Use 4 spaces for indentation (not tabs)
- Maximum line length of 88 characters (we use Black formatter)
- Write descriptive variable and function names
- Include docstrings for all functions, classes, and modules
- Use type hints where appropriate

### Linting

We use the following tools to ensure code quality:

- **Black**: For code formatting
  ```bash
  black .
  ```

- **Flake8**: For style guide enforcement
  ```bash
  flake8
  ```

- **isort**: For import sorting
  ```bash
  isort .
  ```

## Testing Guidelines

- Write tests for all new features and bug fixes
- Maintain or improve test coverage with your changes
- Run tests locally before submitting a PR

```bash
# Run tests
pytest

# Run tests with coverage
pytest --cov=.
```

## Issue Selection Process

1. **Find an issue**
   - Check the [issues tab](https://github.com/OWNER/student-attendance-system/issues)
   - Look for issues labeled `good-first-issue` if you're new to the project
   - Issues labeled `feature-request` are for new enhancements

2. **Comment on the issue**
   - Express your interest in working on the issue
   - Ask any questions you might have about the requirements
   - Wait for a maintainer to assign the issue to you

3. **Work on the issue**
   - Once assigned, follow the development workflow to implement your solution
   - If you're stuck, ask for help in the issue comment thread

## Pull Request Process

1. **Ensure your PR addresses a specific issue**
   - Reference the issue number in your PR description using #issue-number

2. **Fill out the PR template**
   - Describe what your changes do
   - Explain how you've tested your changes
   - List any dependencies that were added or removed

3. **Pass all checks**
   - Your PR must pass all automated tests and checks
   - Address any review comments from maintainers

4. **Code review**
   - A maintainer will review your code
   - You may need to make additional changes based on feedback

5. **Merge**
   - Once approved, a maintainer will merge your PR
   - Celebrate your contribution! 🎉

## Communication

- For quick questions, use the project's discussion board
- For bug reports or feature requests, create an issue
- Be respectful and considerate in all communications

Thank you for contributing to the Student Attendance System!
