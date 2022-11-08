class Library:
    def __init__(self, city, street, zip_code, open_hours: str, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self, *args):
        return f'Adres biblioteki: {self.city}, {self.street}, {self.zip_code} '
