import magazine.Product
from shop.book import Book
from shop.Employee import Employee
from shop.Student import Student
from shop.Order import Order
from shop.Library import Library


biblioteka_1 = Library('Będzin', 'Kasztanowa', '40-400', '9-21', 987123645)
biblioteka_2 = Library('Katowice', 'Czeladzka', '40-410', '10-21', 321123645)

ksiazka_1 = Book('Ulubiona', '11.11.2021', 'Stanisław', 'Beben', 123)
ksiazka_2 = Book('Droga', '11.04.2001', 'Stanisław', 'Beben', 13)
ksiazka_3 = Book('Lepsza', '01.03.2020', 'Wacław', 'Beben', 100)
ksiazka_4 = Book('Ulubiona', '21.03.2000', 'Mojżesz', 'Nowak', 53)
ksiazka_5 = Book('Droga', '11.10.2021', 'Maciej', 'Brac', 64)

pracownik_1 = Employee("Adam", 'Kowalski', '11.10.2021', '11.10.1999', 'Będzin', 'Kasztanowa', '40-400', 987123645)
pracownik_2 = Employee("Tomasz", 'Kowal', '11.10.2011', '01.10.1990', 'Katowice', 'Nowa', '41-400', 987123123)
pracownik_3 = Employee("Maciej", 'Nowak', '21.05.2021', '02.11.1999', 'Chorzów', 'Długa', '40-422', 987172545)

zamowienie_1 = Order("Adam", [34, 46, 69, 32, 90, 59, 90, 80], 'Ulubiona', '11.11.2021', 'Stanisław', 'Beben', 123,
                     '16.11.2022', 'Maciej',
                     'Nowak', '21.05.2021', '02.11.1999', 'Chorzów', 'Długa', '40-422', '987172545')
zamowienie_2 = Order("Tomasz", [34, 46, 69, 32, 90, 59, 90, 80], 'Ulubiona', '11.11.2021', 'Stanisław', 'Beben', 123,
                     '16.11.2022', 'Maciej',
                     'Nowak', '21.05.2021', '02.11.1999', 'Chorzów', 'Długa', '40-422', '987172545')

print(zamowienie_1)
print(zamowienie_2)