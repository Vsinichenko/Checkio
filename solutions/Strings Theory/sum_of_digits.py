#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run sum-of-digits

# The task in this mission is as follows:
# 
# You are given an integer. If it consists of one digit, simply return its value.     If it consists of two or more digits - add them until the number contains only one digit and return it.
# 
# 
# 
# Input:Integer(int).
# 
# Output:Integer(int).
# 
# 
# END_DESC

def sum_digits(num: int) -> int:
    # your code here
    return 0


print("Example:")
print(sum_digits(38))

# These "asserts" are used for self-checking
assert sum_digits(38) == 2
assert sum_digits(0) == 0
assert sum_digits(10) == 1
assert sum_digits(132) == 6
assert sum_digits(232) == 7
assert sum_digits(811) == 1
assert sum_digits(702) == 9

print("The mission is done! Click 'Check Solution' to earn rewards!")