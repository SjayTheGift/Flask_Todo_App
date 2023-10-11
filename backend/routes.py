# app/routes.py
from flask import Blueprint, request, jsonify, make_response
from models import Todo
from database import db

todo_bp = Blueprint('todo', __name__, url_prefix='/todos')

@todo_bp.route('/', methods=['GET'])
def get_todos():
    try:
        todos = Todo.query.all()
        return make_response(jsonify([todo.json() for todo in todos]), 200)
    except:
        return make_response(jsonify({'message': 'error getting todos'}), 500)

@todo_bp.route('create', methods=['POST'])
def create_todo():
    try:
        data = request.get_json()
        new_todo = Todo(title=data['title'], is_complete=data['is_complete'])
        db.session.add(new_todo)
        db.session.commit()
        return make_response(jsonify({'message': 'Todo created successfully'}), 201)
    except:
        return make_response(jsonify({'message': 'error creating todo'}), 500)