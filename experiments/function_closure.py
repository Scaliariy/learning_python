def outer_function(x):
    def inner_function(y):
        return x + y

    return inner_function


closure = outer_function(10)
result = closure(5)  # Здесь closure - это замыкание, и x равно 10
print(result)  # Выведет 15, так как closure сохраняет значение x из внешней функции
