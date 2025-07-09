#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run take-and-return-argument

# 1. Let's make our functionfuncfrom the previous mission more useful. Let it take an argumentarginside brackets. If you have any trouble, see the hints below the description.
# 
# 2. Return the argument value without any changes using keywordreturn.
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