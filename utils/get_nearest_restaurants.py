from loader import restaurants_storage


def get_nearest_restaurant_id(latitude: float, longitude: float, state: int):
    sorted_ids = sorted(restaurants_storage.restaurants, key=lambda r_id: restaurants_storage.restaurants[r_id].calculate_distance(latitude, longitude))
    return sorted_ids[state]


# def get_3_nearest_restaurants(latitude: float, longitude: float, state: int):
#     sorted_restaurants = sorted(restaurants,
#     key=lambda restaurant: restaurant.calculate_distance(latitude, longitude))
#     return sorted_restaurants[state*3:(state*3+3)]
