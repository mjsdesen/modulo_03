from flask import Flask, request, jsonify
from models.task import task as Task
# quando foi executado manualmente, vai ter essa formato __name__ == "__main__":
app = Flask(__name__)

# CRUD
# Create, Read, Update, Delete = Criar, Ler, Atualizar, Deletar
# Tabela: Tarefas

tasks = []
task_id_control = 1

# endpoint: /tasks (POST) cada vez que for criado uma nova tarefa 
@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control
    data = request.get_json()
    new_task = Task(id=task_id_control, title=data['title'], description=data.get('description', ''))
    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify(message='Nova tarefa criada com sucesso!', id=new_task.id), 201


# endpoint: /tasks (GET) para listar todas as tarefas
@app.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]
    return jsonify({"tasks": task_list, "total_tasks": len(task_list)}), 200


# endpoint: /tasks/<int:id> (GET) para buscar uma tarefa específica
@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task = next((task.to_dict() for task in tasks if task.id == id), None)
    if task:
        return jsonify(task), 200
    return jsonify(message='Tarefa não encontrada'), 404


# endpoint: /tasks/<int:id> (PUT) para atualizar uma tarefa específica
@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break
    if task == None:
        return jsonify(message='Tarefa atualizada com sucesso!'), 404
    
    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']
    print(task)
    
    return jsonify(message='Tarefa atualizada com sucesso!')

# endpoint: /tasks/<int:id> (DELETE) para deletar uma tarefa específica
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break
        
    if not task:
        return jsonify(message='Tarefa não encontrada'), 404

    tasks.remove(task)
    return jsonify(message='Tarefa deletada com sucesso!')

# ==================================
# executa o servidor
if __name__ == "__main__":
    # executa o servidor
    app.run(debug=True, host='localhost', port=5000)
