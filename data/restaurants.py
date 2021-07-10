import csv


ONLY_VEGAN = 0
VEGAN_KITCHEN = 1
PARTLY_VEGAN = 2


class Restaurant:
    def __init__(self, name, status, positions, image_link, link, address, coords):
        self.name = name
        self.status = Restaurant.encode_status(status)
        self.positions = positions
        self.image_link = image_link
        self.link = link
        self.address = address
        coords = Restaurant.split_coords(coords)
        self.latitude = coords[0]
        self.longitude = coords[1]

    @staticmethod
    def encode_status(status):
        if status == "Only vegan":
            status = ONLY_VEGAN
        elif status == VEGAN_KITCHEN:
            status = VEGAN_KITCHEN
        else:
            status = PARTLY_VEGAN
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
            restaurants.append(Restaurant(name=row[0], status=row[1], positions=row[2], image_link=row[3], link=row[4],
                                          address=row[5], coords=row[6]))
    return restaurants
