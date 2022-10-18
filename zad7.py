import requests

response = requests.get("https://api.openbrewerydb.org/breweries")


class Brawery:
    def __init__(self, id, name, brewery_type, street, address_2, address_3, city, state,
                 county_province, postal_code, country, longitude, latitude, phone, website_url,
                 updated_at, created_at):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.street = street
        self.address_2 = address_2
        self.address_3 = address_3
        self.city = city
        self.state = state
        self.county_province = county_province
        self.postal_code = postal_code
        self.country = country
        self.longitude = longitude
        self.latitude = latitude
        self.phone = phone
        self.website_url = website_url
        self.updated_at = updated_at
        self.created_at = created_at

    def __str__(self, *args):
        return f'Brawery({self.id},{self.name},{self.brewery_type},{self.street},{self.address_2}, {self.address_3}, ' \
               f'{self.city}, {self.state},{self.county_province}, {self.postal_code},{self.country}, {self.longitude}, ' \
               f'{self.latitude}, {self.phone}, {self.website_url}, {self.updated_at})'




print(response.json())
