
# Class Activity #01: TaskManagerApp

```markdown
# TaskManagerApp with Flask and Docker

This project demonstrates a simple task management application using Flask, Docker, and GitHub Actions for CI/CD. The application exposes endpoints to manage tasks and is containerized using Docker.

## Features

- **Task Management**: Add and list tasks.
- **Flask Web Application**: Simple web server to handle HTTP requests.
- **Dockerized**: Application containerized for easy deployment.
- **GitHub Actions**: Automated CI/CD pipeline to build and push Docker images to Docker Hub.

## Endpoints

- **List Tasks**: `GET /tasks`
- **Add Task**: `GET /calc/add/<task_name>`

## Prerequisites

- Docker
- Docker Hub account
- GitHub account

## Setup

### Clone the Repository

```bash
git clone https://github.com/your-username/TaskManagerApp.git
cd TaskManagerApp
```

### Flask Application Structure

```
TaskManagerApp/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   └── task_manager/
│       ├── __init__.py
│       └── tasks.py
├── tests/
│   └── test_tasks.py
├── Dockerfile
├── .dockerignore
├── requirements.txt
└── README.md
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Flask Application

```bash
export FLASK_APP=app
export FLASK_RUN_HOST=0.0.0.0
flask run
```

### Access the Application

- List tasks: `http://localhost:5000/tasks`
- Add task: `http://localhost:5000/calc/add/<task_name>`

## Docker Instructions

### Build Docker Image

```bash
docker build -t dkay7223/ca3:latest .
```

### Run Docker Container

```bash
docker run -p 5000:5000 dkay7223/ca3:latest
```

### Pull Docker Image from Docker Hub

```bash
docker pull dkay7223/ca3:latest
```

### Run Docker Image from Docker Hub

```bash
docker run -p 5000:5000 dkay7223/ca3:latest
```

## GitHub Actions CI/CD

### Setup GitHub Actions Workflow

Create a `.github/workflows/docker-image.yml` file:

```yaml
name: Build and Push Docker Image

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v2

    - name: Set up Docker Buildx
      uses: docker/setup-buildx-action@v1

    - name: Log in to Docker Hub
      uses: docker/login-action@v2
      with:
        username: ${{ secrets.DOCKER_USERNAME }}
        password: ${{ secrets.DOCKER_PASSWORD }}

    - name: Build and push Docker image
      uses: docker/build-push-action@v3
      with:
        push: true
        tags: dkay7223/ca3:latest
```

### Add GitHub Secrets

- `DOCKER_USERNAME`: Your Docker Hub username.
- `DOCKER_PASSWORD`: Your Docker Hub password.

### Push Changes to GitHub

```bash
git add .
git commit -m "Add Flask app and Docker setup"
git push origin main
```

## Testing the Application

1. **Pull and run the Docker image:**
   ```bash
   docker pull dkay7223/ca3:latest
   docker run -p 5000:5000 dkay7223/ca3:latest
   ```

2. **Access the application:**
   - List tasks: `http://localhost:5000/tasks`
   - Add task: `http://localhost:5000/calc/add/<task_name>`


## License

This project is licensed under the MIT License.


This README file provides an overview of the project, instructions for installation and usage, details on the branching strategy and feature implementation, information on the CI process, and guidelines for contributing.
