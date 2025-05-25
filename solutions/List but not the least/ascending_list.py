#!/usr/bin/env checkio --domain=py run ascending-list

# Determine whether a sequence of elements is ascending such that each of its elements is strictly larger than (and not merely equal to) the preceding element. Empty sequence is considered as ascending.
# 
# 
# 
# Input:Listwith integers(int).
# 
# Output:Logic value(bool).
# 
# The mission was taken from Python CCPS 109 Fall 2018. It is taught for Ryerson Chang School of Continuing Education byIlkka Kokkarinen
# 
# 
# END_DESC

def is_ascending(items: list[int]) -> bool:
    # your code here
    return False


print("Example:")
print(is_ascending([-5, 10, 99, 123456]))

# These "asserts" are used for self-checking
assert is_ascending([-5, 10, 99, 123456]) == True
assert is_ascending([99]) == True
assert is_ascending([4, 5, 6, 7, 3, 7, 9]) == False
assert is_ascending([]) == True
assert is_ascending([1, 1, 1, 1]) == False
assert is_ascending([1, 3, 3, 5]) == False

print("The mission is done! Click 'Check Solution' to earn rewards!")