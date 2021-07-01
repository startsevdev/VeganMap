from aiogram import types
from shapely.geometry import Point, MultiPoint
from shapely.ops import nearest_points

from loader import restaurants


def get_nearest_restaurant(user_location: types.Message):
    nearest_location = get_nearest_location(user_location)
    return get_restaurant(*nearest_location)


def get_nearest_location(user_location: types.Message):
    user_location_point = Point(user_location.location.latitude, user_location.location.longitude)
    restaurants_multipoint = create_restaurants_multipoint()
    nearest_point = get_two_nearest_points(user_location_point, restaurants_multipoint)
    return [nearest_point.x, nearest_point.y]


def create_restaurants_multipoint():
    restaurants_points = []
    for restaurant in restaurants:
        restaurants_points.append(Point(restaurant.latitude, restaurant.longitude))
    return MultiPoint(restaurants_points)


def get_two_nearest_points(user_location_point, restaurants_multipoint):
    two_nearest_points = nearest_points(user_location_point, restaurants_multipoint)
    nearest_point = two_nearest_points[1]
    return nearest_point


def get_restaurant(latitude, longitude):
    for restaurant in restaurants:
        if restaurant.latitude == latitude and restaurant.longitude == longitude:
            return restaurant
