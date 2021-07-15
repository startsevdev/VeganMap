from loader import restaurants


def get_3_nearest_restaurants(latitude: float, longitude: float, state: int):
    sorted_restaurants = sorted(restaurants, key=lambda restaurant: restaurant.calculate_distance(latitude, longitude))
    return sorted_restaurants[state*3:(state*3+3)]

