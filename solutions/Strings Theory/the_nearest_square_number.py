#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run the-nearest-square-number

# You have some number and you are trying to find the nearest square number (a perfect square). Square number is the number the square root of which is an integer. For example, if we start with the number 8, then the two nearby square numbers are 4 (sqrt(4) == 2) and 9 (sqrt(9) == 3). So the answer is 9, because 9 is the nearest.
# 
# 
# 
# 
# 
# Input:An integer(int).
# 
# Output:An integer(int).
# 
# Precondition:
# 0 < number <= 1000000
# 
# 
# 
# END_DESC

def nearest_square(num: int) -> int:
    # your code here
    return 0


print("Example:")
print(nearest_square(8))

# These "asserts" are used for self-checking
assert nearest_square(8) == 9
assert nearest_square(13) == 16

print("The mission is done! Click 'Check Solution' to earn rewards!")