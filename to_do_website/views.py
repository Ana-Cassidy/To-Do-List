from flask import Blueprint, redirect, render_template, url_for, request
from .models import Todo
from . import db

my_view = Blueprint("my_view", __name__)

@my_view.route("/")
def home():
    todo_list = Todo.query.all()
    success = request.args.get("success", None)
    message = request.args.get("message", None)
    edition = request.args.get("edition", None)
    return render_template("index.html", todo_list = todo_list, success=success, message=message, edition=edition)

@my_view.route("/add", methods=["POST"])
def add():
    try:
        task = request.form.get("task")
        new_todo = Todo(task=task)
        db.session.add(new_todo)
        db.session.commit()
        success = "Success! Your task was added to your To Do List!"
        return redirect(url_for("my_view.home", success=success))
    except:
        message = "There was an error adding your task. Please try again"
        return redirect(url_for("my_view.home", message=message))
    
@my_view.route("/update/<todo_id>")
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("my_view.home"))

@my_view.route("/delete/<todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("my_view.home"))

@my_view.route("/edit/<todo_id>", methods=["POST"])
def edit(todo_id):
    try:
        todo = Todo.query.filter_by(id=todo_id).first()
        edit_task = request.form.get("edit_task")
        todo.task = edit_task
        db.session.commit()
        edition = "Your task was successfully edited!"
        return redirect(url_for("my_view.home", edition=edition))
    except:
        error = "It was not possible to edit your task. Please try again"
        return redirect(url_for("my_view.home", error=error))