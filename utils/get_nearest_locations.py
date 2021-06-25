from aiogram import types
from shapely.geometry import Point, MultiPoint
from shapely.ops import nearest_points
import asyncio


def get_nearest_location(user_location: types.Message):
    places_locations = [Point(59.968660, 30.317764), Point(59.92837, 30.31232), Point(59.931900, 30.370297)]
    places_locations_multi_point = MultiPoint(places_locations)
    user_location_point = Point(user_location.location.latitude, user_location.location.longitude)
    nearest_locations = nearest_points(user_location_point, places_locations_multi_point)
    return "{0}, {1}".format(nearest_locations[1].x, nearest_locations[1].y)
