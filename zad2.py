from zad1 import Student


class Library:
    def __init__(self, city, street, zip_code, open_hours: str, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self, *args):
        return f'Adres biblioteki: {self.city}, {self.street}, {self.zip_code} '


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self, *args):
        return f'Dane pracownika: {self.first_name}, {self.last_name}, {self.hire_date}'


class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self, *args):
        return f'Dane o książce: {self.library}, {self.publication_date}, {self.author_name}, {self.author_surname}, {self.number_of_pages}'


class Order(Student, Book, Employee):
    def __init__(self, name, marks, library, publication_date, author_name, author_surname, number_of_pages,
                 first_name, last_name, hire_date, birth_date, city, street, zip_code, phone, order_date):
        Student.__init__(self, name, marks)
        Book.__init__(self, library, publication_date, author_name, author_surname, number_of_pages)
        Employee.__init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone)
        self.order_date = order_date

    def __str__(self, *args):
        return f'Dane o zamówieniu, Imie zamawiającego: {self.name}. Dane o książce: {self.library}, ' \
               f'{self.publication_date}, {self.author_name}. Dane pracownika: {self.first_name}, {self.last_name}, ' \
               f'{self.hire_date}'


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
