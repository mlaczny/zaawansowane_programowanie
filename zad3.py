def even_number(number) -> bool:
    return number % 2 == 0


x = even_number(5)
print("Liczba parzysta") if x else print("Liczba nieparzysta")
y = even_number(4)
print("Liczba parzysta") if y else print("Liczba nieparzysta")