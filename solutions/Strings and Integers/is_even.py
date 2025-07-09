#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run is-even

# Check if the given number is even or not. Your function should returnTrueif the number is even, andFalseif the number is odd.
# 
# Input:An integer(int).
# 
# Output:Logic value(bool).
# 
# 
# END_DESC

def is_even(num: int) -> bool:
       
    return True if  num % 2 ==0 else False


print("Example:")
print(is_even(2))

# These "asserts" are used for self-checking
assert is_even(2) == True
assert is_even(5) == False
assert is_even(0) == True

print("The mission is done! Click 'Check Solution' to earn rewards!")