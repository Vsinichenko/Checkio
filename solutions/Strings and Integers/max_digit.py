#!/usr/bin/env checkio --domain=py run max-digit

# You have a number and you need to determine which digit in this number is the biggest.
# 
# 
# 
# Input:A positive integer(int).
# 
# Output:An integer 0-9(int).
# 
# 
# END_DESC

def max_digit(value: int) -> int:
    ls = list(str(value))
    return int(max(ls))
    


print("Example:")
print(max_digit(10))

# These "asserts" are used for self-checking
assert max_digit(0) == 0
assert max_digit(52) == 5
assert max_digit(634) == 6
assert max_digit(1) == 1
assert max_digit(10000) == 1

print("The mission is done! Click 'Check Solution' to earn rewards!")