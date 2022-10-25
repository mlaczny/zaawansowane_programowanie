def even_elements(numbers):
    for n in range(10):
        if numbers[n] % 2 == 0:
            print(numbers[n])

numbers = [1, 4, 2, 5, 2, 6, 1, 56, 7, 2]
even_elements(numbers)
