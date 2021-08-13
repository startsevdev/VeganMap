import csv
from aiogram import types

from geopy import distance


# RESTAURANT STATUSES
ONLY_VEGAN = 0
VEGAN_KITCHEN = 1
PARTLY_VEGAN = 2
FEW_OPTIONS = 3


class Restaurant:
    def __init__(self, name, status, positions, image_id, link, address, coords):
        self.name = name
        self.status = Restaurant.encode_status(status)
        self.positions = positions
        self.image_id = image_id
        self.link = link
        self.address = address
        self.latitude, self.longitude = Restaurant.parse_coords(coords)
        self.menu_description = self.create_menu_description()

    def create_message_content(self, user_latitude: float, user_longitude: float):
        if self.image_id == "":
            image_id = "AgACAgIAAxkBAAIH7GDsYzx_ZBpw6q_J4b0BZ_jmeL6sAAJ6szEbrgABaEuSFdUE77IV4gEAAwIAA3MAAyAE"
        else:
            image_id = self.image_id

        # text = "<b>{name}</b>\n\n{menu_description}\n<a href='{link}'>Instagram</a>\n\n{address}\n{distance} от вас".format(
        text = "<b>{name}</b> • <a href='{link}'>Instagram</a>\n\n{menu_description}\n\n{address}\n{distance} от вас".format(
            name=self.name, menu_description=self.menu_description, link=self.link, address=self.address,
            distance=Restaurant.format_distance(self.calculate_distance(user_latitude, user_longitude)))
        return image_id, text

    def calculate_distance(self, latitude: float, longitude: float):
        user_location = (latitude, longitude)
        restaurant_location = (self.latitude, self.longitude)
        return distance.distance(user_location, restaurant_location).km

    def create_menu_description(self):
        if self.status == ONLY_VEGAN:
            return "100% vegan"
        elif self.status == PARTLY_VEGAN:
            return "Больше трёх веганских позиций"
        elif self.status == FEW_OPTIONS:
            return "Веганские позиции: " + self.positions
        elif self.status == VEGAN_KITCHEN:
            return "Кухня – 100% vegan. По напиткам уточняйте"

    @staticmethod
    def encode_status(status):
        if status == "Only vegan":
            status = ONLY_VEGAN
        elif status == "Vegan kitchen":
            status = VEGAN_KITCHEN
        elif status == "Partly vegan":
            status = PARTLY_VEGAN
        else:
            status = FEW_OPTIONS
        return status

    @staticmethod
    def parse_coords(coords):
        if coords != "":
            split_coords = coords.split(", ")
            latitude = split_coords[0]
            longitude = split_coords[1]
        else:
            latitude = 0.0
            longitude = 0.0
        return latitude, longitude

    @staticmethod
    def format_distance(distance_km):
        if distance_km < 1:
            return "{0} м".format(round(distance_km * 1000))
        else:
            return "{0} км".format(round(distance_km, 1))


def create_restaurants():
    restaurants = {}
    r_id = 0
    with open('data/restaurants.csv', newline='') as File:
        reader = csv.reader(File)
        header = next(reader)
        for row in reader:
            restaurants[r_id] = Restaurant(name=row[0], status=row[1], positions=row[2], image_id=row[3], link=row[4],
                                           address=row[5], coords=row[6])
            r_id += 1
    return restaurants
