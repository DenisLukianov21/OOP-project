from flask import Flask, render_template, request, redirect, url_for
from core.tasks import Task
from core.db import Session, TaskDB

app = Flask(__name__, static_folder='static')


@app.route("/", methods=["GET", "POST"])
def index():
    """
    Handles the '/' route for both GET and POST requests.
    """
    with Session() as session:
        tasks = session.query(TaskDB).filter(TaskDB.status == False).all()
    if request.method == "POST":
        task_name = request.form.get("Name")
        task_description = request.form.get("Description")
        task = Task(name=task_name, description=task_description)
        with Session() as session:
            session.add(TaskDB(name=task.name,
                               description=task.description,
                               status=task.status,
                               time=task.time))
            session.commit()
        return redirect(url_for('index'))
    return render_template('index.html', tasks=tasks)


@app.route("/delete/<int:id>")
def delete(id):
    """
    Delete a task based on the provided id.

    Args:
        id (int): The id of the task to be deleted.
    """
    with Session() as session:
        task = session.query(TaskDB).get(id)
        session.delete(task)
        session.commit()
    return redirect(url_for('index'))


@app.route("/done/<int:id>")
def done(id):
    """
    Marks a task as done based on the provided task ID.

    Args:
        id (int): The ID of the task to mark as done.
    """
    with Session() as session:
        task = session.query(TaskDB).get(id)
        task.status = True
        session.commit()
    return redirect(url_for('index'))


@app.route("/about")
def about():
    """
    A description of the about project.
    """
    return render_template('about.html')


@app.route('/completed')
def completed():
    """
    Retrieves all completed tasks from the database and renders the
    'completed.html' template with the tasks.
    """
    with Session() as session:
        tasks = session.query(TaskDB).filter(TaskDB.status == True).all()
    return render_template('completed.html', tasks=tasks)


if __name__ == "__main__":
    app.run(debug=True)
