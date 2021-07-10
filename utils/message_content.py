from data.restaurants import Restaurant


def get_restaurant_content(restaurant: Restaurant):
    image = restaurant.image_link
    text = "{name}\n{link}\n{address}".format(name=restaurant.name, link=restaurant.link, address=restaurant.address)
    return image, text
