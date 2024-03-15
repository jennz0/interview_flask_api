from controller import *
from flask import Blueprint

todo_Blueprint = Blueprint('todo', __name__, url_prefix = '/todo')
todo_Blueprint.add_url_rule('/', view_func = TodoListView.as_view("todolist"), methods=["GET", "POST"])