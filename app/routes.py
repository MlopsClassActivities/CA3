from flask import current_app as app, jsonify, request
from .task_manager.tasks import TaskManager

task_manager = TaskManager()

@app.route('/tasks', methods=['GET'])
def list_tasks():
    return jsonify(task_manager.list_tasks())

@app.route('/calc/<operation>/<task>', methods=['GET'])
def calc(operation, task):
    if operation == "add":
        task_manager.add_task(task)
        return jsonify({"message": "Task added successfully"})
    return jsonify({"error": "Invalid operation"}), 400
