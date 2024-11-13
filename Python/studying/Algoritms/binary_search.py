"""Show's how works binary search"""
import random


def binary_search(numbers: list, number: int):
    """
    Shows how works binary search
    """
    iteration_count: int = 0
    low: int = 0
    high: int = len(numbers) - 1
    while low <= high:
        iteration_count += 1
        mid: int = (low + high) // 2
        guess: int = numbers[mid]
        if guess == number:
            return iteration_count
        if guess > number:
            high: int = mid - 1
        else:
            low: int = mid + 1
    return None


# Creating sorted list
my_list: list[int] = sorted([number for number in range(1, 240000)])

# Choosing two random numbers from list and taking count iterations
for random_number in random.choices(my_list, k=2):
    print(f"\nFor {random_number}:\n"
          f"Iteration count: {binary_search(my_list, random_number)}")



