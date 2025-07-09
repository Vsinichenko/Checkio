#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run reverse-every-ascending

# Create and return a newIterablethat contains the same elements as the givenlistitems, but with the reversed order of the elements inside every maximal strictly ascending subsequence.    This function should not modify the contents of the original list.
# 
# 
# 
# Input:Listof integers(int).
# 
# Output:Listor anotherIterable(tuple,iterator,generator) of integers(int).
# 
# Precondition:given sequence includes only integers.
# 
# The mission was taken from Python CCPS 109 Fall 2018. It’s being taught for Ryerson Chang School of Continuing Education byIlkka Kokkarinen
# 
# 
# END_DESC

from collections.abc import Iterable


def reverse_ascending(items: list[int]) -> Iterable[int]:
    # your code here
    return []


print("Example:")
print(list(reverse_ascending([1, 2, 3, 4, 5])))

# These "asserts" are used for self-checking
assert list(reverse_ascending([1, 2, 3, 4, 5])) == [5, 4, 3, 2, 1]
assert list(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3])) == [
    10,
    7,
    5,
    4,
    8,
    7,
    2,
    3,
    1,
]
assert list(reverse_ascending([5, 4, 3, 2, 1])) == [5, 4, 3, 2, 1]
assert list(reverse_ascending([])) == []
assert list(reverse_ascending([1])) == [1]
assert list(reverse_ascending([1, 1])) == [1, 1]
assert list(reverse_ascending([1, 1, 2])) == [1, 2, 1]

print("The mission is done! Click 'Check Solution' to earn rewards!")