def print_in_loop(numbers):
    num = []
    for x in numbers:
        x = x * 2
        num.append(x)
    return num


def print_list_comprehension(numbers):
    return [x * 2 for x in numbers]


numbers = [1, 5, 3, 6, 34]

print(print_in_loop(numbers))
print(print_list_comprehension(numbers))
