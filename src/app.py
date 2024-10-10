from flask import Flask, jsonify, request

app = Flask(__name__)


todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]


@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    print("Incoming request with the following body", request_body)

    
    todos.append(request_body)
    
    
    return jsonify(todos), 200  


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    try:
       
        removed_todo = todos.pop(position)
        print(f"Deleted todo at position {position}: {removed_todo}")
        return jsonify(todos), 200  
    except IndexError:
        
        return jsonify({"error": "Invalid position"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
