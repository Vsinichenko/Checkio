#!/home/valentyna-sinichenko/miniconda3/bin/checkio --domain=py run easy-unpack

# 
# 
# Your mission here is to create a function that gets atupleand returns atuplewith only 3 elements - the first, third and second element from the last for the giventuple.
# 
# One important thing worth pointing out is that you need to use index in order to extract elements from thetuple. Pay attention, index counting starts from 0, not from 1. Which means that if you need to get the first element from thetupleelements, you should doelements[0], and the second element iselements[1].
# 
# 
# 
# Input:Atuple, at least 3 elements long.
# 
# Output:Atuple.
# 
# 
# END_DESC

def easy_unpack(elements: tuple) -> tuple:
    # your code here
    return ()


print("Example:")
print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))

# These "asserts" are used for self-checking
assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
assert easy_unpack((6, 3, 7)) == (6, 7, 3)

print("The mission is done! Click 'Check Solution' to earn rewards!")