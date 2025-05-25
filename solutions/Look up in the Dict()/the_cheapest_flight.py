#!/usr/bin/env checkio --domain=py run the-cheapest-flight

# 
# 
# "We need to fly home as cheaply as possible so that more money is left for gifts. Aunt Lidia asked for different kinds of cheeses, and Vasia wanted a new toy car. I’ve been looking at the schedule for quite a while and I’m starting to think that some planes are flying in vain".
# 
# As the input you get the flight schedule as list, each element of which is the price of a direct flight between 2 cities (list of 3 elements - 2 city names as a string, and a flight price).
# 
# Planes fly in both directions and the price in both directions is the same. There is a possibility that there are no direct flights between cities.
# 
# Find the price of the cheapest flight between cities that are given as the 2nd and 3rd arguments. In case the flight can not be performed, return 0.
# 
# Input:3 arguments: the flight schedule as a list of lists, city of departure and destination city as strings.
# 
# Output:The best price as integer.
# 
# Preconditions:price is always integer;the flight schedule contains at least one element;both cities are in the schedule.
# 
# 
# END_DESC

import math

def get_max_trip_length(num_cities:int)-> int:
    max_lenth=0
    for r in range(2, num_cities+1):
        max_lenth+=math.perm(num_cities, r)
    return max_lenth


assert get_max_trip_length(4)==12+24+24
assert get_max_trip_length(3)==12


def is_meaningful_route(trip_1: str, trip_2: str) -> bool:
    for city in trip_1[:-1]:
        if city in trip_2:
            return False
    return True


def cheapest_flight(costs: list, a: str, b: str) -> int:
    cities = set()
    routes = set()
    simple_routes_dict = {}

    for cost in costs:
        start_city = cost[0]
        end_city = cost[1]
        price=cost[-1]
        direct_route =  start_city+end_city
        return_route = end_city+start_city
        routes.add(direct_route)
        routes.add(return_route)
        cities.add(start_city)
        cities.add(end_city)

        if start_city in simple_routes_dict:
            simple_routes_dict[start_city][end_city]=price
        else:
            simple_routes_dict[start_city]={}
            simple_routes_dict[start_city][end_city]=price

        if end_city in simple_routes_dict:
            simple_routes_dict[end_city][start_city]=price
        else:
            simple_routes_dict[end_city]={}
            simple_routes_dict[end_city][start_city]=price

    simple_routes = routes.copy()
        
    for i in range(get_max_trip_length(len(cities))+1):
        for begin_route in routes.copy():
            for end_route in simple_routes:
                # AFHB and BD combine into AFHBD
                if begin_route[-1]==end_route[0] and is_meaningful_route(begin_route, end_route):
                    new_route=begin_route[:-1]+end_route
                    routes.add(new_route)
       
    costs_dict = dict.fromkeys(routes, None) 
    # calculate the costt of each trip 
    for route in costs_dict.keys(): # TODO fix price calculation here
        cost=0
        # key example ABC
        for i in range(len(route)-1): 
            price = simple_routes_dict[route[i]][route[i+1]]
            cost+=price
        costs_dict[route]=cost

    # now, get the cheapest trip
    possible_trips = []
    for route in costs_dict.keys():
        if route.startswith(a) and route.endswith(b):
            possible_trips.append(route)

    if not possible_trips:
        return 0

    min_cost = costs_dict[possible_trips[0]]
    for trip in possible_trips:
        if costs_dict[trip]<min_cost:
            min_cost=costs_dict[trip]
    return min_cost   

print("Example:")
assert (
    cheapest_flight(
        [
            ["A", "C", 40],
            ["A", "B", 20],
            ["A", "D", 20],
            ["B", "C", 50],
            ["D", "C", 70],
        ],
        "D",
        "C",
    )
    == 60
)

print(cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "A", "C"))

# These "asserts" are used for self-checking
assert (
    cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "A", "C") == 70
)
assert (
    cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "C", "A") == 70
)

assert (
    cheapest_flight([["A", "C", 100], ["A", "B", 20], ["D", "F", 900]], "A", "F") == 0
)
assert (
    cheapest_flight(
        [["A", "B", 10], ["A", "C", 15], ["B", "D", 15], ["C", "D", 10]], "A", "D"
    )
    == 25
)

print("The mission is done! Click 'Check Solution' to earn rewards!")