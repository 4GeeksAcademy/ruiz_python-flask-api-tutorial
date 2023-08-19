from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    {"label": "My first task", "done": False},
    {"label": "My second task", "done": False}
]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    try:
        request_data = request.json
        new_todo = {"label": request_data.get("label"), "done": False}
        todos.append(new_todo)
        return jsonify(todos), 200  # 201 Created status code
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # 500 Internal Server Error


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    try:
        if position < 0 or position >= len(todos):
            return jsonify({"error": "Invalid position"}), 400
        
        # Remove the task at the specified position
        deleted_task = todos.pop(position)
        
        return jsonify(todos), 200  # Return the updated list of todos
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # 500 Internal Server Error


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)