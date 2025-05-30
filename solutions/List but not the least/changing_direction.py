#!/home/valentyna-sinichenko/miniconda3/bin/checkio --domain=py run changing-direction

# You are given a sequence of integers. Your task in this mission is to find, how many times the sorting direction was changed in the given sequence. If the elements are equal - the previous sorting direction remains the same, if the sequence starts from the same elements - look for the next different to determine the sorting direction.
# 
# Let's look at the scheme:
# 
# 
# 
# There are three sorting directions:on the chunk1, 2, 2- up (increasing);on the chunk2, 1- down (decreasing);and on the chunk1, 2, 2- up again.So, you have two points of changing the sorting direction: #1 - from up to down, and #2 - from down to up. That's the result your function should return.
# 
# Input:Listof integers(int).
# 
# Output:An integer(int).
# 
# Preconditions:the sequence is non-empty;the elements are positive integers.
# 
# 
# END_DESC

def changing_direction(elements: list[int]) -> int:
    # your code here
    return 0


print("Example:")
print(changing_direction([1, 2, 3, 4, 5]))

# These "asserts" are used for self-checking
assert changing_direction([1, 2, 3, 4, 5]) == 0
assert changing_direction([1, 2, 3, 2, 1]) == 1
assert changing_direction([1, 2, 2, 1, 2, 2]) == 2

print("The mission is done! Click 'Check Solution' to earn rewards!")