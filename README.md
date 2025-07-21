# Python Task Manager API

A simple REST API for task management built with Flask.

## 🚀 Features

- Create, read, update, and delete tasks
- RESTful API design
- JSON responses
- In-memory storage (database integration coming soon)

## 📋 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API information and available endpoints |
| GET | `/tasks` | Get all tasks |
| POST | `/tasks` | Create a new task |
| GET | `/tasks/<id>` | Get a specific task |
| PUT | `/tasks/<id>` | Update a task |
| DELETE | `/tasks/<id>` | Delete a task |

## 🛠️ Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd python-task-manager