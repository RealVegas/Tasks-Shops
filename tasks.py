# Task manager
# self.time = datetime.strftime(datetime.now(), 'H%:M%')

from datetime import datetime


class Task:

    def __init__(self, name: str, deadline: str, status: bool = True) -> None:
        self.name = name
        self.deadline = deadline
        self.status = status

    def add_task(self) -> dict[str, str]:
        self.name = input('Введите название задачи: ')
        self.deadline = input('Введите срок выполнения задачи (в формате Час:Мин): ')
        return {'name': self.name, 'deadline': self.deadline}

class TaskManager(Task):

    def __init__(self, name, deadline, status=True):
        super().__init__(name, deadline, status=True)
        self.tasks: list[dict] = []

    def add_task(self) -> None:
        one_task = super().add_task()
        self.tasks.append(one_task)

    def set_complete(self, index) -> None:
        self.tasks[index]['status'] = False

    def get_active(self) -> None:
        for item in self.tasks:
            if item['status']:
                print(f'Название задачи: {self.name}\nCрок выполнения: {self.deadline}\n')

    def __str__(self):
        for item in self.tasks:
            if item['status']:
                print(f'Название задачи: {self.name}\nCрок выполнения: {self.deadline}\n')

                return f'Название задачи: {self.name}\nCрок выполнения: {self.deadline}\n'



TaskManager(name='Задача1', deadline='11:00')
TaskManager.add_task
# Task(name='Задача2', deadline='12:00')
# Task(name='Задача3', deadline='14:00')
# Task(name='Задача4', deadline='15:00')
# Task(name='Задача5', deadline='18:00')



# print(TaskManager(name='Задача6', deadline='19:00'))