from service import TodoService
from flask import jsonify, request
from flask.views import MethodView


class TodoListView(MethodView):
    def __init__(self):
        self.todo_service = TodoService()
    
    def get(self):
        todo_list = self.todo_service.get_todo_list()
        return jsonify({"todos": [todo.serialize() for todo in todo_list]})
    
    def post(self):
        data = request.json
        todo_info = {
            "description" : data["description"],
            "status" : data["status"]
        }
        success, message = self.todo_service.create_todo(todo_item=todo_info)

        if success:
            return jsonify({"message": "successful create"}), 201
        else:
            return jsonify({"message": "create failed"}), 400
