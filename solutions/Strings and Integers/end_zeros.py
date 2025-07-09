#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run end-zeros

# Try to find out how many zeros a given number has at the end.
# 
# 
# 
# Input:A non-negative integer(int).
# 
# Output:An integer(int).
# 
# 
# END_DESC

def end_zeros(a: int) -> int:
    # your code here
    return 0


print("Example:")
print(end_zeros(10))

# These "asserts" are used for self-checking
assert end_zeros(0) == 1
assert end_zeros(1) == 0
assert end_zeros(10) == 1
assert end_zeros(101) == 0
assert end_zeros(245) == 0
assert end_zeros(100100) == 2

print("The mission is done! Click 'Check Solution' to earn rewards!")