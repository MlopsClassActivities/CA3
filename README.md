
# Class Activity #01: TaskManagerApp

## Overview

TaskManagerApp is a simple command-line task manager application that allows users to add, list, and delete tasks. This project is designed to demonstrate basic software development practices including branching, feature implementation, and continuous integration using GitHub Actions.

## Features

1. **Add Task**: Add a new task to the task list.
2. **List Tasks**: Display all the tasks in the task list.
3. **Delete Task**: Remove a specified task from the task list.

## Project Structure
```
CA1/
├── .github/
│   └── workflows/
│       └── ci.yml
├── CA1/
│   ├── __init__.py
│   ├── main.py
│   └── tasks.py
├── tests/
│   └── test_tasks.py
├── .gitignore
├── README.md
└── requirements.txt
```
- `CA1/main.py`: The main entry point of the application.
- `CA1/tasks.py`: Contains the `TaskManager` class with methods to add, list, and delete tasks.
- `tests/test_tasks.py`: Unit tests for the `TaskManager` class.
- `.github/workflows/ci.yml`: GitHub Actions workflow for continuous integration.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/CA1.git
    cd CA1
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the application:
```bash
python -m CA1.main
```

You will be presented with a menu to add, list, or delete tasks.

## Development

### Branching Strategy

Each feature is developed in its own branch. The branches are named according to the member's roll number:

- `main`: Main branch containing the project scaffolding.
- `member1_roll_no`: Branch for Member 1's feature implementation (Add Task).
- `member2_roll_no`: Branch for Member 2's feature implementation (List Tasks).
- `member3_roll_no`: Branch for Member 3's feature implementation (Delete Task).

### Implementing Features

1. **Member 1 (Add Task)**:
    - Switch to your branch:
        ```bash
        git checkout member1_roll_no
        ```
    - Implement the feature in `CA1/tasks.py`.
    - Commit and push your changes:
        ```bash
        git add .
        git commit -m "Implemented add task feature"
        git push origin member1_roll_no
        ```

2. **Member 2 (List Tasks)**:
    - Switch to your branch:
        ```bash
        git checkout member2_roll_no
        ```
    - Implement the feature in `CA1/tasks.py`.
    - Commit and push your changes:
        ```bash
        git add .
        git commit -m "Implemented list tasks feature"
        git push origin member2_roll_no
        ```

3. **Member 3 (Delete Task)**:
    - Switch to your branch:
        ```bash
        git checkout member3_roll_no
        ```
    - Implement the feature in `CA1/tasks.py`.
    - Commit and push your changes:
        ```bash
        git add .
        git commit -m "Implemented delete task feature"
        git push origin member3_roll_no
        ```

### Continuous Integration

This project uses GitHub Actions for continuous integration. The workflow is defined in `.github/workflows/ci.yml` and runs on every push and pull request. It includes the following steps:

- Check out the code.
- Set up Python.
- Install dependencies.
- Lint the code with flake8.
- Run unit tests with pytest.

## Testing

To run the tests locally:
```bash
pytest
```

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License.


This README file provides an overview of the project, instructions for installation and usage, details on the branching strategy and feature implementation, information on the CI process, and guidelines for contributing.
