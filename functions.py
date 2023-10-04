FILEPATH = "todos.txt"


def get_todos(filepath_local=FILEPATH):
    with open(filepath_local, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_local, filepath_local=FILEPATH):
    with open(filepath_local, 'w') as file_local:
        file_local.writelines(todos_local)
