import csv

from . import statuses


class Restaurant:
    def __init__(self, name, status, positions, image_id, link, address, coords):
        self.name = name
        self.status = Restaurant.encode_status(status)
        self.positions = positions
        self.image_id = image_id
        self.link = link
        self.address = address
        coords = Restaurant.split_coords(coords)
        self.latitude = coords[0]
        self.longitude = coords[1]

    @staticmethod
    def encode_status(status):
        if status == "Only vegan":
            status = statuses.ONLY_VEGAN
        elif status == "Vegan kitchen":
            status = statuses.VEGAN_KITCHEN
        elif status == "Partly vegan":
            status = statuses.PARTLY_VEGAN
        else:
            status = statuses.FEW_OPTIONS
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

    def get_menu_description(self):
        if self.status == statuses.ONLY_VEGAN:
            return "100% vegan"
        elif self.status == statuses.PARTLY_VEGAN:
            return "Больше трех веганских позиций"
        elif self.status == statuses.FEW_OPTIONS:
            return self.positions
        elif self.status == statuses.VEGAN_KITCHEN:
            return "Кухня – 100% vegan. По напиткам уточняйте"


def create_restaurants():
    restaurants = []
    with open('data/restaurants.csv', newline='') as File:
        reader = csv.reader(File)
        header = next(reader)
        for row in reader:
            restaurants.append(Restaurant(name=row[0], status=row[1], positions=row[2], image_id=row[3], link=row[4],
                                          address=row[5], coords=row[6]))
    return restaurants
