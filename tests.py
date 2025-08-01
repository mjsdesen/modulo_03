import pytest
import requests

# CRUD
BASE_URL = "http://localhost:5000/"
task = []

def test_create_task():
    new_task_data = {
        "title": "Test Task",
        "description": "This is a test task."
    }
    response = requests.post(BASE_URL + "tasks", json=new_task_data)
    assert response.status_code == 201
    response_json = response.json()
    assert 'message' in response_json
    assert response_json['message'] == 'Nova tarefa criada com sucesso!'
    assert 'id' in response_json
    task.append(response_json['id'])  # Store the created task ID for later tests

def test_get_tasks():
    response = requests.get(BASE_URL + "tasks")
    assert response.status_code == 200
    response_json = response.json()
    assert 'tasks' in response_json
    assert 'total_tasks' in response_json
    
    
def test_get_task_by_id():
    if task:
        task_id = task[0]
        response = requests.get(BASE_URL + f"tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json() 
        assert 'id' in response_json
        assert response_json['id'] == task_id
        
def test_update_task():
    if task:
        task_id = task[0]
        updated_data = {
            "title": "Updated Task",
            "description": "This is an updated test task.",
            "completed": True
        }
        response = requests.put(BASE_URL + f"tasks/{task_id}", json=updated_data)
        assert response.status_code == 200
        response_json = response.json()
        assert 'message' in response_json
        assert response_json['message'] == 'Tarefa atualizada com sucesso!'
        
        # nova requisição para verificar se a tarefa foi atualizada
        response = requests.get(BASE_URL + f"tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert 'id' in response_json
        assert response_json['id'] == task_id
        assert response_json['title'] == updated_data['title']
        assert response_json['description'] == updated_data['description']
        assert response_json['completed'] == updated_data['completed']
        
def test_delete_task():
    if task:
        task_id = task[0]
        response = requests.delete(BASE_URL + f"tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert 'message' in response_json
        assert response_json['message'] == 'Tarefa deletada com sucesso!'
        
        # Verificar se a tarefa foi realmente deletada
        response = requests.get(BASE_URL + f"tasks/{task_id}")
        assert response.status_code == 404
        response_json = response.json()
        assert 'message' in response_json
        assert response_json['message'] == 'Tarefa não encontrada'