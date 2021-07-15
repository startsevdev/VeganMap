from aiogram import types

from loader import restaurants


def get_3_nearest_restaurants(latitude: float, longitude: float):
    sorted_restaurants = sorted(restaurants, key=lambda restaurant: restaurant.calculate_distance(latitude, longitude))
    return sorted_restaurants[0:3]


# def get_nearest_restaurant(user_location: types.Message):
#     user_location = (user_location.location.latitude, user_location.location.longitude)
#     nearest_restaurant = 0
#     min_distance = 20037.5
#
#     for restaurant in restaurants:
#         restaurant_location = (restaurant.latitude, restaurant.longitude)
#         distance_between = distance.distance(user_location, restaurant_location).km
#
#         if distance_between < min_distance:
#             min_distance = distance_between
#             nearest_restaurant = restaurant
#
#     return nearest_restaurant
