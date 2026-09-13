from flask import Flask, request, jsonify
from models.tasks import Task

app = Flask(__name__)

tasks = []
task_id_control = 1

@app.route("/tasks", methods=['POST'])
def create_task():
  global task_id_control
  data = request.get_json()
  new_task = Task(id=task_id_control, title=data['title'], description=data.get('description', ""))
  task_id_control += 1
  tasks.append(new_task)
  print(tasks)
  return jsonify({ "message": "Task criada com sucesso!" })

@app.route("/tasks", methods=['GET'])
def get_tasks():
  task_list = [task.to_dict() for task in tasks]

  output = {
    "tasks": [
      {
        "tasks": task_list,
        "total_tasks": len(task_list)
      }
    ]
  }

  return jsonify(output)

@app.route("/tasks/<int:id>", methods=['GET'])
def get_task(id: int):
  task = None
  for t in tasks:
    if t.get_id() == id: 
      return jsonify(t.to_dict())
  return jsonify({"message": "Task não encontrada pelo ID"}), 404

@app.route("/tasks/<int:id>", methods=['PUT'])
def put_task(id):
  data = request.get_json()
  for i ,task in enumerate(tasks):
    if task.get_id() == id:
      updated_task = Task(id=id, title=data['title'], description=data.get('description', ''), completed=data.get('completed', False))
      tasks[i] = updated_task
      return jsonify({ "message": f"Deu Update!" })
  return jsonify({ "message": f"Task não encontrada! O id {id} não existe!" })

if __name__ == "__main__":
  app.run(debug=True)