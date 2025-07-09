#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run number-of-sides

# You are given a list of coordinates of the vertices of the triangles (A list of tuples of 3 tuples of 2 integers) into which a polygon is divided.These share at least one side with the other triangle (which also shares two vertices).You have to return the number of sides of the original polygon as an integer.
# 
# Examples:
# 
# 
# 
# 
# assert number_of_sides([((1, 1), (1, 3), (3, 3)), ((1, 1), (3, 1), (3, 3))]) == 4
# assert number_of_sides([((1, 1), (2, 1), (2, 3)), ((2, 1), (2, 3), (3, 1))]) == 3
# assert number_of_sides([((1, 1), (2, 3), (3, 1)), ((2, 3), (3, 1), (4, 3)),
#                         ((2, 3), (3, 5), (4, 3)), ((3, 1), (4, 3), (5, 1))]) == 3
# NOTE:That polygon has no holes.
# 
# Input:The list of coordinates of the triangles (A list of tuples of 3 tuples of 2 integers)(int).
# 
# Output:The number of sides (An integer)(int).
# 
# Precondition:x >= 0, y >= 0
# 
# 
# END_DESC

Coordinate = tuple[int, int]
Triangle = tuple[Coordinate, Coordinate, Coordinate]


def number_of_sides(triangles: list[Triangle, ...]) -> int:
    # your code here
    return 0


print("Example:")
print(number_of_sides([((1, 3), (3, 3), (1, 1)), ((3, 3), (3, 1), (1, 1))]))

# These "asserts" are used for self-checking
assert number_of_sides([((1, 3), (3, 3), (1, 1)), ((3, 3), (3, 1), (1, 1))]) == 4
assert number_of_sides([((1, 1), (2, 3), (2, 1)), ((2, 3), (3, 1), (2, 1))]) == 3
assert (
    number_of_sides(
        [
            ((1, 3), (3, 3), (2, 2)),
            ((3, 3), (3, 1), (2, 2)),
            ((3, 1), (1, 1), (2, 2)),
            ((1, 1), (1, 3), (2, 2)),
        ]
    )
    == 4
)
assert (
    number_of_sides(
        [
            ((3, 5), (4, 3), (2, 3)),
            ((4, 3), (5, 1), (3, 1)),
            ((3, 1), (1, 1), (2, 3)),
            ((2, 3), (4, 3), (3, 1)),
        ]
    )
    == 3
)
assert (
    number_of_sides(
        [
            ((6, 10), (11, 7), (1, 7)),
            ((11, 7), (9, 1), (1, 7)),
            ((9, 1), (3, 1), (1, 7)),
        ]
    )
    == 5
)

print("The mission is done! Click 'Check Solution' to earn rewards!")