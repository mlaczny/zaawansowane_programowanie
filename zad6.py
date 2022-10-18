def add_list(first: list, second: list) -> list:
    third = first + second
    return [x ** 3 for x in list(set(third))]


first = [3, 464, 67, 3, 8, 2, 758, 26, 0]
second = [3, 464, 6, 245, 4563, 7, 643, 3, 8, 2, 758, 26, 0]
print(add_list(first, second))
