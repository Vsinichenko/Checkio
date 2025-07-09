#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run remove-all-after

# Not all of the elements are important. What you need to do here is to remove all of the elements after the given one from sequence.
# 
# 
# 
# For illustration, we have a sequence[1, 2, 3, 4, 5]and we need to remove all the elements that go after3- which are4and5.
# 
# We have two edge cases here:if a cutting element cannot be found, then the sequence shouldn't be changed;if the sequence is empty, then it should remains empty.
# 
# Input:Listof integers(int).
# 
# Output:Listor otherIterable(tuple,iterator,generator...) of integers(int).
# 
# 
# END_DESC

from collections.abc import Iterable


def remove_all_after(items: list[int], border: int) -> Iterable[int]:
    # your code here
    return []


print("Example:")
print(list(remove_all_after([1, 2, 3, 4, 5], 3)))

# These "asserts" are used for self-checking
assert list(remove_all_after([1, 2, 3, 4, 5], 3)) == [1, 2, 3]
assert list(remove_all_after([1, 1, 2, 2, 3, 3], 2)) == [1, 1, 2]
assert list(remove_all_after([1, 1, 2, 4, 2, 3, 4], 2)) == [1, 1, 2]
assert list(remove_all_after([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
assert list(remove_all_after([], 0)) == []
assert list(remove_all_after([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7]

print("The mission is done! Click 'Check Solution' to earn rewards!")