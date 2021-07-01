from aiogram import types
from geopy import distance

from loader import restaurants


def get_nearest_restaurant(user_location: types.Message):
    user_location = (user_location.location.latitude, user_location.location.longitude)
    nearest_restaurant = 0
    min_distance = 191.5

    for restaurant in restaurants:
        restaurant_location = (restaurant.latitude, restaurant.longitude)
        distance_between = distance.distance(user_location, restaurant_location).km

        if distance_between < min_distance:
            min_distance = distance_between
            nearest_restaurant = restaurant

    return nearest_restaurant
