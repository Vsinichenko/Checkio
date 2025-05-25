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

def cheapest_flight(costs: list, a: str, b: str) -> int:
    cities = set()
    routes = set()
    for cost in costs:
        direct_route = cost[0]+cost[1]
        return_route = cost[1]+cost[0]
        routes.add(direct_route)
        routes.add(return_route)
        cities.add(cost[0])
        cities.add(cost[1])
        
    for i in rane(len(costs)*2): # TODO how long can it be
        for begin_route in routes:
            for end_route in routes:
                # AFHB and BD combine into AFHBD
                if begin_route[-1]==end_route[0]:
                    routes.add(begin_route[:1]+end_route)
       
     costs_dict = dict.fromkeys(routes, None) 
                           
                           
        
        
        
        
        


print("Example:")
print(cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "A", "C"))

# These "asserts" are used for self-checking
assert (
    cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "A", "C") == 70
)
assert (
    cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "C", "A") == 70
)
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