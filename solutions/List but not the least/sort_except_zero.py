#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run sort-except-zero

# Sort the integers in sequence in sequence. But the position of zeros should not be changed.
# 
# Input:Listof integers(int).
# 
# 
# 
# Output:Listor anotherIterable(tuple,generator,iterator) of integers(int).
# 
# Precondition:
# 
# All numbers are non-negative.
# 
# 
# END_DESC

from collections.abc import Iterable


def except_zero(items: list[int]) -> Iterable[int]:
    # your code here
    return []


print("Example:")
print(list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])))

# These "asserts" are used for self-checking
assert list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])) == [1, 3, 0, 0, 4, 4, 5, 0, 7]
assert list(except_zero([0, 2, 3, 1, 0, 4, 5])) == [0, 1, 2, 3, 0, 4, 5]
assert list(except_zero([0, 0, 0, 1, 0])) == [0, 0, 0, 1, 0]
assert list(except_zero([4, 5, 3, 1, 1])) == [1, 1, 3, 4, 5]
assert list(except_zero([0, 0])) == [0, 0]

print("The mission is done! Click 'Check Solution' to earn rewards!")