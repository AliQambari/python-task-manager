from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

# In-memory task storage (we'll use database later)
tasks = []
task_id_counter = 1

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to Task Manager API",
        "version": "1.0.0",
        "endpoints": [
            "GET /tasks - Get all tasks",
            "POST /tasks - Create new task",
            "GET /tasks/<id> - Get specific task",
            "PUT /tasks/<id> - Update task",
            "DELETE /tasks/<id> - Delete task"
        ]
    })

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks})

@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_counter
    
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({"error": "Title is required"}), 400
    
    task = {
        "id": task_id_counter,
        "title": data['title'],
        "description": data.get('description', ''),
        "completed": False,
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat()
    }
    
    tasks.append(task)
    task_id_counter += 1
    
    return jsonify(task), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)