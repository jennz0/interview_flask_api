from flask import Flask
from blueprint import todo_Blueprint
from database import initialize_db

app = Flask(__name__)

app.register_blueprint(todo_Blueprint)
initialize_db()


if __name__ == '__main__':
    app.run(debug=True)