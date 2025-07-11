#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run isometric-strings

# Maybe it's a cipher? Maybe, but we don’t know for sure.
# 
# Maybe you can call it"homomorphism"? I wish I knew this word before.
# 
# You need to check that the string A is isometric to the string B. There exists a function that turns characters from A into characters in the same spot in B.
# 
# Characters in A correspond to a unique character value in B. Characters in B are allowed to correspond to multiple character values in A.
# 
# Input:Two strings(str).
# 
# Output:Logic value(bool).
# 
# Precondition:
# both strings have the same length.
# 
# 
# END_DESC

def isometric_strings(a: str, b: str) -> bool:
    # your code here
    return False


print("Example:")
print(isometric_strings("add", "egg"))

# These "asserts" are used for self-checking
assert isometric_strings("add", "egg") == True
assert isometric_strings("foo", "bar") == False
assert isometric_strings("bar", "foo") == True
assert isometric_strings("", "") == True
assert isometric_strings("all", "all") == True
assert isometric_strings("gogopy", "doodle") == False
assert isometric_strings("abba", "cccc") == True

print("The mission is done! Click 'Check Solution' to earn rewards!")