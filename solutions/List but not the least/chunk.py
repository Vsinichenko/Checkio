#!/home/valentyna-sinichenko/miniconda3/bin/checkio --domain=py run chunk

# You have a lot of work to do, so you might want to split it into smaller pieces. This way you'll know which piece you'll do on Monday, which will be for Tuesday and so on.
# 
# Splitlistinto smaller lists of the same size (chunks). The last chunk can be smaller than the default chunk-size. If the given list is empty, then you shouldn't have any chunks at all.
# 
# 
# 
# Input:Two arguments.Listand chunk size as integer(int).
# 
# Output:Listor anotherIterable(tuple,generator,iterator) with chunkedlists.
# 
# Precondition:chunk-size > 0
# 
# 
# END_DESC

from collections.abc import Iterable


def chunking_by(items: list[int], size: int) -> Iterable[list[int]]:
    # your code here
    return [[]]


print("Example:")
print(list(chunking_by([5, 4, 7, 3, 4, 5, 4], 3)))

# These "asserts" are used for self-checking
assert list(chunking_by([5, 4, 7, 3, 4, 5, 4], 3)) == [[5, 4, 7], [3, 4, 5], [4]]
assert list(chunking_by([3, 4, 5], 1)) == [[3], [4], [5]]
assert list(chunking_by([5, 4], 7)) == [[5, 4]]
assert list(chunking_by([], 3)) == []
assert list(chunking_by([4, 4, 4, 4], 4)) == [[4, 4, 4, 4]]

print("The mission is done! Click 'Check Solution' to earn rewards!")