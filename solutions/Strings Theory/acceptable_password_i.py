#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run acceptable-password-i

# You are at the beginning of a password series. Every mission is based on the previous one. The missions that follow will become slightly more complex.
# 
# In this mission, you need to create a password verification function.
# 
# The verification condition is:
# 
# the length should be bigger than 6.Input:A string(str).
# 
# Output:A logic value(bool).
# 
# 
# END_DESC

def is_acceptable_password(password: str) -> bool:
    # your code here
    return False


print("Example:")
print(is_acceptable_password("short"))

# These "asserts" are used for self-checking
assert is_acceptable_password("short") == False
assert is_acceptable_password("muchlonger") == True
assert is_acceptable_password("ashort") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")