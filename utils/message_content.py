from data.restaurants import Restaurant
from data import statuses


def get_restaurant_content(restaurant: Restaurant):
    image_id = restaurant.image_id
    text = "*{name}*\n{menu_description}\n{link}\n{address}".format(
        name=restaurant.name, menu_description=restaurant.get_menu_description(), link=restaurant.link,
        address=restaurant.address)
    return image_id, text
