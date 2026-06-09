from database.db import SessionLocal
from database.models import Task
def add_task(title):

    session = SessionLocal()

    task = Task(
        title=title
    )

    session.add(task)

    session.commit()

    session.close()

    return "Task added."
def get_tasks():

    session = SessionLocal()

    tasks = session.query(
        Task
    ).all()

    session.close()

    return tasks
def complete_task(title):

    session = SessionLocal()

    task = session.query(
        Task
    ).filter_by(
        title=title
    ).first()

    if not task:

        session.close()

        return "Task not found."

    task.completed = True

    session.commit()

    session.close()

    return "Task completed."