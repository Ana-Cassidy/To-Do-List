from . import db
from datetime import datetime

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    task = db.Column(db.String(300), unique = True)
    complete = db.Column(db.Boolean, default = False)
    date = db.Column(db.String(300))
    time = db.Column(db.String(300))
    finish_date = db.Column(db.String(300))
    finish_time = db.Column(db.String(300))