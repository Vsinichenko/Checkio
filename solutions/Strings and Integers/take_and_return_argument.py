#!/usr/bin/env checkio --domain=py run take-and-return-argument

# 1. Let's make our functionfuncmore usual. Let it take some argumentarg.
# 
# 2. Return the argument value without any changes.
# 
# 
# END_DESC

# Taken from mission Empty Function

# write your code here
def func(arg):
    return arg


print("Example:")
print(func(3))

# These "asserts" are used for self-checking
assert func(3) == 3
assert func("string") == "string"
assert func(True) == True

print("The mission is done! Click 'Check Solution' to earn rewards!")