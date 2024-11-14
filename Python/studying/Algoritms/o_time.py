
def work_time(items_count: int) -> int:
    new_number: int = 2
    degree: int = 2

    while new_number < items_count:
        degree += 1
        new_number *= 2
    else:
        return degree - 1

for lenght in [100, 10000, 1000000000]:
    print(f"For array of lenght {lenght} items the time is ~{work_time(lenght)}ms")
