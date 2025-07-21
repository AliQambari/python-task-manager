from functools import wraps
from flask import jsonify

def validate_json(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not request.is_json:
            return jsonify({"error": "Content-Type must be application/json"}), 400
        return f(*args, **kwargs)
    return decorated_function

def find_task_by_id(task_id):
    return next((task for task in tasks if task['id'] == task_id), None)