"""Student Task Manager - task logic."""


class TaskManager:
    def __init__(self):
        self.tasks = []
        self._next_id = 1

    def add_task(self, title):
        task = {'id': self._next_id, 'title': title, 'completed': False}
        self.tasks.append(task)
        self._next_id += 1
        return task
