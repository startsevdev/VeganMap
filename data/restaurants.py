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
        self.menu_description = self.create_menu_description()

        coords = Restaurant.split_coords(coords)
        self.latitude = coords[0]
        self.longitude = coords[1]

    def create_message_content(self, message: types.Message):
        image_id = self.image_id
        text = "<b>{name}</b>\n{menu_description}\n<a href='{link}'>Instagram</a>\n\n{address}\n{distance} км от вас".format(
            name=self.name, menu_description=self.menu_description, link=self.link,
            address=self.address, distance=round(self.calculate_distance(message), 2))
        return image_id, text

    def calculate_distance(self, message: types.Message):
        user_location = (message.location.latitude, message.location.longitude)
        return distance.distance(user_location, (self.latitude, self.longitude)).km

    def create_menu_description(self):
        if self.status == ONLY_VEGAN:
            return "100% vegan"
        elif self.status == PARTLY_VEGAN:
            return "Больше трех веганских позиций"
        elif self.status == FEW_OPTIONS:
            return self.positions
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
    def split_coords(coords):
        if coords != "":
            split_coords = coords.split(",")
            latitude = float(split_coords[0])
            longitude = float(split_coords[1])
        else:
            latitude = 0.0
            longitude = 0.0
        return [latitude, longitude]


def create_restaurants():
    restaurants = []
    with open('data/restaurants.csv', newline='') as File:
        reader = csv.reader(File)
        header = next(reader)
        for row in reader:
            restaurants.append(Restaurant(name=row[0], status=row[1], positions=row[2], image_id=row[3], link=row[4],
                                          address=row[5], coords=row[6]))
    return restaurants
