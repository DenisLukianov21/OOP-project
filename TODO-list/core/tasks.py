import datetime


class Task:
    """Represents a task with a name, description, status and timestamp."""

    def __init__(self, name: str, description: str) -> None:
        """
        Initialize a new Task instance.

        Args:
            name (str): The name of the task.
            description (str): The description of the task.
        """
        self.name = name
        self.description = description
        self.status = False
        self.time = datetime.datetime.now()

    def __str__(self) -> str:
        """Return a string representation of the Task."""
        return (
            f"Name: {self.name}\n"
            f"Description: {self.description}\n"
            f"Status: {self.status}\n"
            f"Time: {self.time}\n"
        )

    def complete_task(self) -> None:
        """Set the status of the task to True, indicating completion."""
        self.status = True
