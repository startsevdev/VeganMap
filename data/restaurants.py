import csv

ONLY_VEGAN = 0
VEGAN_KITCHEN = 1
PARTLY_VEGAN = 2


class Restaurant:
    def __init__(self, name, status, positions, image_link, link, coords):
        self.name = name
        self.image_link = image_link
        self.link = link
        self. coords = coords

        if status == "Only vegan":
            self.status = ONLY_VEGAN
        elif status == VEGAN_KITCHEN:
            self.status = VEGAN_KITCHEN
        else:
            self.status = PARTLY_VEGAN


def create_restaurants():
    restaurants = []

    with open('data/restaurants.csv', newline='') as File:
        reader = csv.reader(File)
        for row in reader:
            restaurants.append(Restaurant(row[0], row[1], row[2], row[3], row[4], row[5]))
    return restaurants
