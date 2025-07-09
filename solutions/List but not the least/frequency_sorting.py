#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run frequency-sorting

# Sort the given sequence so that its elements should be grouped and those groups end up in the decreasing frequency order, that is, the number of times element appears in the sequence. If two elements have the same frequency, their groups should end up according to the natural order of elements. For example:
# 
# 
# 
# If you want to practice more with the similar case, trySort Array by Element Frequencymission.
# 
# Input:Listof integers(int).
# 
# Output:Listor anotherIterable(tuple,iterator,generator) of integers(int).
# 
# Preconditions:listlength <= 100;max number <= 100.
# 
# The mission was taken fromPython CCPS 109. It is taught forRyerson Chang School of Continuing EducationbyIlkka Kokkarinen
# 
# 
# END_DESC

from collections.abc import Iterable


def frequency_sorting(numbers: list[int]) -> Iterable[int]:
    # replace this for solution
    return []


print("Example:")
print(list(frequency_sorting([1, 2, 3, 4, 5])))

# These "asserts" are used for self-checking
assert list(frequency_sorting([1, 2, 3, 4, 5])) == [1, 2, 3, 4, 5]
assert list(frequency_sorting([3, 4, 11, 13, 11, 4, 4, 7, 3])) == [
    4,
    4,
    4,
    3,
    3,
    11,
    11,
    7,
    13,
]

print("The mission is done! Click 'Check Solution' to earn rewards!")