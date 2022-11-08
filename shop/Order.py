from shop.book import Book
from shop.Employee import Employee
from shop.Student import Student


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