#!/usr/bin/env checkio --domain=py run golden-pyramid

# Our Robo-Trio need to train for future journeys and treasure hunts.    Stephan has built a special flat model of a pyramid. Now the robots can train for speed gold running.    They start at the top of the pyramid and must collect gold in each room,    choose to take the left or right path and continue down to the next level.    To optimize their gold runs, Stephan need to know the maximum amount of gold that can be collected in one run.
# 
# Consider a list of lists in which the first list has one integer and each consecutive list has one more integer then the last. Such a list of lists would look like a pyramid. You should write a program that will help Stephan find the highest possible sum on the most profitable route down the pyramid. All routes down the pyramid involve stepping down and to the left or down and to the right.
# 
# Tips:Think of each step down to the left as moving to the same index location or to the right as one index location higher. Be very careful if you plan to use recursion here.
# 
# 
# 
# Input:A pyramid as a list of lists of integers.
# 
# Output:The maximum possible sum as an integer.
# 
# Preconditions:0 < len(pyramid) ≤ 20;all(all(0 < x < 10 for x in row) for row in pyramid).
# 
# 
# END_DESC

def get_sub_pyramid(ls: list[list[int]], mode: str) -> list[list[int]]:
    new_ls = []
    for el in ls[1:]:
        if mode=="r":
            new_ls.append(el[1:])
        elif mode=="l":
            new_ls.append(el[:-1])
    return new_ls


def count_gold(pyramid: list[list[int]]) -> int:
    if len(pyramid)==1:
        return pyramid[0][0]
    else:
        l_pyramid = get_sub_pyramid(pyramid, mode="l")
        r_pyramid = get_sub_pyramid(pyramid, mode="r")
        return max(count_gold(l_pyramid), count_gold(r_pyramid))+pyramid[0][0]



print("Example:")
print(count_gold([[1], [2,3], [8,9,10], [11,12,13,14]]))

# These "asserts" are used for self-checking
assert (
    count_gold(
        [
            [1],
            [2, 3],
            [3, 3, 1],
            [3, 1, 5, 4],
            [3, 1, 3, 1, 3],
            [2, 2, 2, 2, 2, 2],
            [5, 6, 4, 5, 6, 4, 3],
        ]
    )
    == 23
)
assert (
    count_gold(
        [
            [1],
            [2, 1],
            [1, 2, 1],
            [1, 2, 1, 1],
            [1, 2, 1, 1, 1],
            [1, 2, 1, 1, 1, 1],
            [1, 2, 1, 1, 1, 1, 9],
        ]
    )
    == 15
)
assert count_gold([[9], [2, 2], [3, 3, 3], [4, 4, 4, 4]]) == 18
assert (
    count_gold(
        [[2], [7, 9], [0, 8, 6], [4, 7, 6, 8], [0, 5, 5, 4, 1], [9, 1, 0, 1, 6, 9]]
    )
    == 35
)
assert (
    count_gold(
        [
            [4],
            [3, 0],
            [5, 1, 1],
            [2, 0, 2, 0],
            [1, 1, 1, 8, 3],
            [5, 3, 4, 8, 2, 8],
            [1, 0, 5, 0, 4, 3, 1],
        ]
    )
    == 30
)
assert (
    count_gold(
        [
            [6],
            [7, 9],
            [3, 8, 3],
            [3, 4, 0, 2],
            [6, 9, 9, 6, 8],
            [3, 7, 0, 8, 2, 2],
            [0, 6, 3, 0, 0, 6, 7],
        ]
    )
    == 49
)
assert (
    count_gold(
        [
            [6],
            [0, 6],
            [3, 0, 7],
            [0, 4, 2, 9],
            [4, 4, 3, 6, 9],
            [3, 1, 0, 5, 9, 0],
            [8, 9, 7, 7, 3, 4, 5],
        ]
    )
    == 50
)
assert (
    count_gold(
        [
            [6],
            [6, 9],
            [7, 1, 4],
            [6, 9, 9, 7],
            [1, 6, 7, 9, 7],
            [5, 7, 2, 6, 0, 9],
            [1, 2, 2, 6, 0, 1, 6],
            [8, 5, 0, 3, 1, 4, 3, 1],
            [9, 6, 4, 1, 1, 9, 3, 7, 9],
            [5, 8, 4, 3, 5, 4, 5, 1, 8, 3],
        ]
    )
    == 66
)

print("The mission is done! Click 'Check Solution' to earn rewards!")