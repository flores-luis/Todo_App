import git
from flask import render_template,redirect,request
#from flask.wrappers import Response

#do not think I will create a login page
#import re
#from flask_bcrypt import Bcrypt
from flask_app import app
from flask_app.models.task import Task
#from datetime import datetime

@app.route('/update_server', methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('https://github.com/flores-luis/Todo_App')
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboardPage')
def dashboard():
    list = Task.get_all_tasks()
    return render_template('dashboard.html', task_list=list)

@app.route('/createtask')
def createtask():
    return render_template('create.html')

@app.route('/addnewtask',methods=['POST'])
def addtask():
    data = {
        "task_name": request.form["task_name"],
        "notes": request.form["notes"],
        "due_date": request.form["due_date"],
        "priority_level": request.form["priority_level"]
    }
    Task.save(data)
    return redirect('/dashboardPage')

@app.route('/update/<int:id>')
def edit_task(id):
    data = {
        "id":id
    }
    return render_template("update.html",edit=Task.get_one(data))

@app.route('/update_task',methods=['POST'])
def update():
    data = {
        "id": request.form['id'],
        "task_name": request.form["task_name"],
        "notes": request.form["notes"],
        "due_date": request.form["due_date"],
        "priority_level": request.form["priority_level"],
    }
    Task.update(data)
    return redirect('/dashboardPage')

@app.route('/view/<int:id>')
def view_task(id):
    data = {
        "id":id
    }
    return render_template("read.html",task=Task.get_one(data))

@app.route('/delete/<int:id>')
def delete_task(id):
    data = {
        "id":id
    }
    Task.delete(data)
    return redirect('/dashboardPage')
