from flask import Blueprint, redirect, render_template, url_for, request
from .models import Todo
from . import db
from datetime import datetime

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
        date = request.form.get("new_task_date")
        time = request.form.get("new_task_time")
        new_todo = Todo(task=task, date=date, time=time)
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

@my_view.route("/update_date/<todo_id>", methods=["POST"])
def update_date(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    finish_date = request.form.get("finish_date")
    todo.finish_date = finish_date
    db.session.commit()
    return redirect(url_for("my_view.home"))

@my_view.route("/update_time/<todo_id>", methods=["POST"])
def update_time(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    finish_time = request.form.get("finish_time")
    if finish_time:
        todo.finish_time = finish_time
        db.session.commit()
    return redirect(url_for("my_view.home"))


@my_view.route("/delete/<todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("my_view.home"))

@my_view.route("/edit_task/<todo_id>", methods=["POST"])
def edit_task(todo_id):
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
    
@my_view.route("/edit_date/<todo_id>", methods=["POST"])
def edit_date(todo_id):
    try:
        todo = Todo.query.filter_by(id=todo_id).first()
        edit_date = request.form.get("edit_date")
        todo.date = edit_date
        db.session.commit()
        edition = "Your task was successfully edited!"
        return redirect(url_for("my_view.home", edition=edition))
    except:
        error = "It was not possible to edit your task. Please try again"
        return redirect(url_for("my_view.home", error=error))
    
@my_view.route("/edit_time/<todo_id>", methods=["POST"])
def edit_time(todo_id):
    try:
        todo = Todo.query.filter_by(id=todo_id).first()
        edit_time = request.form.get("edit_time")
        todo.time = edit_time
        db.session.commit()
        edition = "Your task was successfully edited!"
        return redirect(url_for("my_view.home", edition=edition))
    except:
        error = "It was not possible to edit your task. Please try again"
        return redirect(url_for("my_view.home", error=error))