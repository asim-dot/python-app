from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory task storage
tasks = [
    {"id": 1, "title": "Buy groceries", "done": False},
    {"id": 2, "title": "Learn Python", "done": True}
]
next_id = 3

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks), 200

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        return jsonify(task), 200
    return jsonify({"error": "Task not found"}), 404

@app.route('/tasks', methods=['POST'])
def create_task():
    global next_id
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({"error": "Title is required"}), 400
    task = {"id": next_id, "title": data['title'], "done": data.get('done', False)}
    tasks.append(task)
    next_id += 1
    return jsonify(task), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)