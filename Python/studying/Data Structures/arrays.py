from array import array

# Создание массива
my_array: array = array('i', [1, 2, 3, 4])

# Добавление элемента
my_array.append(5)

# Удаление элемента
my_array.remove(2)

# Доступ по индексу
print(my_array[0])  # Вывод: 1