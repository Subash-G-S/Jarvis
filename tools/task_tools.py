from services.task_service import (
    add_task,
    get_tasks,
    complete_task
)


def create_task(task):

    return add_task(task)


def show_tasks():

    tasks = get_tasks()

    if not tasks:

        return "No tasks found."

    result = ""

    for i, task in enumerate(
        tasks,
        start=1
    ):

        status = (
            "Completed"
            if task.completed
            else "Pending"
        )

        result += (
            f"{i}. {task.title}"
            f" [{status}]\n"
        )

    return result


def mark_task_complete(task):

    return complete_task(task)