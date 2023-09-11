def get_todos(filepath_local="files/todos.txt"):
    with open(filepath_local, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_local, filepath_local="files/todos.txt"):
    with open(filepath_local, 'w') as file_local:
        file_local.writelines(todos_local)


while True:
    user_action = input("Type show, add, edit, complete or exit: ")

    if user_action.startswith('add'):
        todo = user_action[4:]
        todos = get_todos()
        todos.append(todo + '\n')
        write_todos(todos)

    elif user_action.startswith('show'):
        todos = get_todos()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            todos = get_todos()
            number = int(user_action[5:])
            new_todo = input("New value is: ")
            todos[number - 1] = new_todo + '\n'
            write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('complete'):
        try:
            todos = get_todos()
            number = int(user_action[9:])
            removed_todo = todos.pop(number - 1).strip('\n')
            write_todos(todos)
            message = f"Todo \"{removed_todo}\" was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("Command is not valid!")

print("Bye!")
