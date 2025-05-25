#!/usr/bin/env checkio --domain=py run move-zeros

# You are given a list of integers.    Move all zeros in the list to the end of it.    The order of non-zero elements should not change.
# 
# Input:A list of integers.
# 
# Output:A list or another Iterable (tuple, genenator, iterator) of integers.
# 
# Examples:
# 
# assert list(move_zeros([0, 1, 0, 3, 12])) == [1, 3, 12, 0, 0]
# assert list(move_zeros([0])) == [0]
# 
# END_DESC

from typing import Iterable


def move_zeros(items: list[int]) -> Iterable[int]:
    # your code here
    return []


print("Example:")
print(list(move_zeros([0, 1, 0, 3, 12])))

# These "asserts" are used for self-checking
assert list(move_zeros([0, 1, 0, 3, 12])) == [1, 3, 12, 0, 0]
assert list(move_zeros([0])) == [0]

print("The mission is done! Click 'Check Solution' to earn rewards!")