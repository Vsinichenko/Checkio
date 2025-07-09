#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run how-deep

# You are given a tuple that consists of integers and other tuples, which in turn can also contain tuples.
# 
# Your task is to find out how deep this structure is or how deep the nesting of these tuples is.
# 
# For example, in the(1, 2, 3)tuple the depth of nesting is 1. And in the(1, 2, (3,))tuple the depth of nesting is 2, since one of the elements of the first tuple is also a tuple. And in the(1, 2, (3, (4,)))tuple the depth of nesting is 3, since one of the elements of the first tuple is a tuple, but since inside it contains another tuple, it increases the depth by one, so the nesting depth turns out to be 3.
# 
# It’s important to note that an empty tuple also increases the depth of the structure, that is,()- indicates the nesting depth 1,((),)- indicates the nesting depth 2.
# 
# Input:Tuple of tuples of tuples...of integers.
# 
# Output:Integer.
# 
# Precondition:Given iterables have to be well founded.
# 
# 
# END_DESC

def how_deep(structure: tuple) -> int:
    # your code here
    return 0


print("Example:")
print(how_deep((1, 2, 3)))

# These "asserts" are used for self-checking
assert how_deep((1, 2, 3)) == 1
assert how_deep((1, 2, (3,))) == 2
assert how_deep((1, 2, (3, (4,)))) == 3
assert how_deep(()) == 1
assert how_deep(((),)) == 2
assert how_deep((((),),)) == 3
assert how_deep((1, (2,), (3,))) == 2
assert how_deep((1, ((),), (3,))) == 3

print("The mission is done! Click 'Check Solution' to earn rewards!")