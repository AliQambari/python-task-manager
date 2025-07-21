import requests
import json

BASE_URL = "http://localhost:5000"

def test_api():
    print("Testing Task Manager API...")
    
    # Test 1: Get API info
    response = requests.get(f"{BASE_URL}/")
    print(f"API Info: {response.status_code}")
    
    # Test 2: Create a task
    task_data = {
        "title": "Test Task",
        "description": "This is a test task"
    }
    response = requests.post(f"{BASE_URL}/tasks", 
                           json=task_data, 
                           headers={"Content-Type": "application/json"})
    print(f"Create Task: {response.status_code}")
    
    if response.status_code == 201:
        task = response.json()
        task_id = task['id']
        
        # Test 3: Get all tasks
        response = requests.get(f"{BASE_URL}/tasks")
        print(f"Get All Tasks: {response.status_code}")
        
        # Test 4: Get specific task
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        print(f"Get Specific Task: {response.status_code}")
        
        # Test 5: Update task
        update_data = {"completed": True}
        response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=update_data)
        print(f"Update Task: {response.status_code}")
        
        # Test 6: Complete task
        response = requests.put(f"{BASE_URL}/tasks/{task_id}/complete")
        print(f"Complete Task: {response.status_code}")
        
        # Test 7: Delete task
        response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
        print(f"Delete Task: {response.status_code}")

if __name__ == "__main__":
    test_api()