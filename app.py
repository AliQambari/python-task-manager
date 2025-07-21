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
@app.route('/tasks/<int:task_id>/complete', methods=['PUT'])
def complete_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    
    task['completed'] = True
    task['updated_at'] = datetime.now().isoformat()
    
    return jsonify(task)
from flask import Flask, jsonify, request
from datetime import datetime
from utils import validate_json, find_task_by_id

# ... existing code ...

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = find_task_by_id(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(task)

@app.route('/tasks/<int:task_id>', methods=['PUT'])
@validate_json
def update_task(task_id):
    task = find_task_by_id(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    
    data = request.get_json()
    
    # Update fields if provided
    if 'title' in data:
        task['title'] = data['title']
    if 'description' in data:
        task['description'] = data['description']
    if 'completed' in data:
        task['completed'] = data['completed']
    
    task['updated_at'] = datetime.now().isoformat()
    
    return jsonify(task)

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    task = find_task_by_id(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    
    tasks = [t for t in tasks if t['id'] != task_id]
    return jsonify({"message": "Task deleted successfully"})
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)