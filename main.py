while True:
    user_action = input("Type show, add, edit, complete or exit: ")

    if user_action.startswith('add'):
        todo = user_action[4:]
        # context provider/manager:
        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()
        todos.append(todo + '\n')
        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith('show'):
        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()
        # list comprehension:
        # todos = [todo.strip('\n') for todo in todos]
        for index, item in enumerate(todos):
            item = item.strip('\n')
            # f-string:
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()
        number = int(user_action[5:])
        new_todo = input("New value is: ")
        todos[number - 1] = new_todo + '\n'
        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith('complete'):
        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()
        number = int(user_action[9:])
        removed_todo = todos.pop(number - 1).strip('\n')
        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)
        message = f"Todo \"{removed_todo}\" was removed from the list."
        print(message)

    elif user_action.startswith('exit'):
        break

    else:
        print("Command is not valid!")

print("Bye!")
