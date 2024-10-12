main : set = {1, 2, 3, 4, 5, 6, 7}
other : set = {5, 6, 7, 8}

print(f"&: {main & other}")
print(f"|: {main | other}")
print(f"-: {main - other}")
print(f"^: {main ^ other}")


# Python has first class functions
def create_adder(x):
    def adder(y):
        return x + y
    return adder

add_10 = create_adder(10)
add_10(3)   # => 13

# Closures in nested functions:
# We can use the nonlocal keyword to work with variables in nested scope which shouldn't be declared in the inner functions.
def create_avg():
    total = 0
    count = 0
    def avg(n):
        nonlocal total, count
        total += n
        count += 1
        return total/count
    return avg
avg = create_avg()
avg(3)  # => 3.0
avg(5)  # (3+5)/2 => 4.0
avg(7)  # (8+7)/3 => 5.0