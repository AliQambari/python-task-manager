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

Create virtual environment:

bashpython -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies:

bashpip install -r requirements.txt

Run the application:

bashpython app.py
The API will be available at http://localhost:5000
📝 Usage Examples
Create a task:
bashcurl -X POST http://localhost:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Learn Git", "description": "Complete Git basics course"}'
Get all tasks:
bashcurl http://localhost:5000/tasks
🎯 Project Goals
This project is part of a learning curriculum focusing on:

✅ Git basics and version control
🔄 RESTful API development
📦 Python package management
🚀 Deployment preparation
📊 Code documentation

🔄 Development Roadmap
Phase 1: Basic API (Current)

 Basic CRUD operations
 Flask setup
 Git integration

Phase 2: Database Integration (Next)

 SQLite database
 Data persistence
 Database migrations

Phase 3: Advanced Features

 User authentication
 Task categories
 Due dates and reminders
 API documentation with Swagger

🤝 Contributing

Fork the repository
Create a feature branch: git checkout -b feature-name
Commit your changes: git commit -m 'Add some feature'
Push to the branch: git push origin feature-name
Submit a pull request
