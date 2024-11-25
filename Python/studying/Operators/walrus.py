"""
The ":=" operator, known as the "walrus operator", was introduced in Python 3.8.
It allows you to assign values to variables in expressions, which can simplify code and make it more readable."""

"""
Usage examples
"""

""" Example 1: Assignment and use in the condition """

# Without walrus operator
value = input("Enter something: ")
if value:
    print(f"You entered: {value}")

# With walrus operator
if value := input("Enter something: "):
    print(f"You entered: {value}")


"""
In this value, the value entered by the user is assigned to the variable value and immediately used in the fundamental if.
Example 2: Using in a loop
"""

# Без моржового оператора
data = []
while True:
    value = input("Введите число (или 'exit' для выхода): ")
    if value == 'exit':
        break
    data.append(int(value))

# С моржовым оператором
data = []
while (value := input("Введите число (или 'exit' для выхода): ")) != 'exit':
    data.append(int(value))

# Здесь := позволяет одновременно проверять условие и присваивать значение.

# Преимущества
# Сокращение кода: Уменьшается количество строк кода.
# Читаемость: Упрощает понимание, когда присваивание происходит в условиях.
# Ограничения
# Оператор не может использоваться в выражениях, где не допускается присваивание (например, в списковых включениях, если нет явного контекста).
# Использование моржового оператора может сделать ваш код более лаконичным и удобным, но стоит использовать его с осторожностью, чтобы не ухудшить читаемость.