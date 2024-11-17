from array import array

# Creating array
my_array: array = array('i', [1, 2, 3, 4])

# Adding element
my_array.append(5)

# Deleting element
my_array.remove(2)

# Getting element by index
print(my_array[0])  # Output: 1