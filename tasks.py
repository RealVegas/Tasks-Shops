# Task manager

class Task:

    def __init__(self) -> None:
        self.task_list: list[dict] = []

    def add_task(self) -> None:
        task_name: str = input('Введите название задачи: ')
        task_deadline: str = input('Введите срок выполнения задачи (в формате Час:Мин): ')
        task_status: bool = True

        self.task_list.append({'name': task_name, 'deadline': task_deadline, 'status': task_status})

    def set_complete(self) -> None:
        task_index: str = input('Введите номер задачи: ')

        if task_index.isdigit() and int(task_index) <= len(self.task_list):
            self.task_list[int(task_index) - 1]['status'] = False

    def __str__(self) -> str:
        active_list: str = ''
        for number, item in enumerate(self.task_list, 1):
            if item['status']:
                active_list += f'{number}. Название задачи: {item["name"]}, Cрок выполнения: {item["deadline"]}\n'

        return active_list


tsk = Task()

print('1. Добавить задачу в список')
print('2. Отметить задачу как выполненную')
print('3. Вывести список активных задач')
print('4. Закончить работу\n')

work = True

while work:
    option = input('Выберите действие: ')

    match option:
        case '1':
            tsk.add_task()
            print('Задача добавлена в список\n')
        case '2':
            tsk.set_complete()
            print('Задача помечена как выполненная\n')
        case '3':
            print('Список задач:')
            print(tsk)
        case '4':
            print('Программа завершает свою работу')
            work = False
        case _:
            print('Такого действия нет в списке, повторите ввод')