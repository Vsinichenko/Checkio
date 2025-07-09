#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run escher-symmetry

# M. C. Escherwas a Dutch graphic artist who created incredible illustrations which were inspired by mathematics. For example, he filled the canvas with self-similar objects, whose contours fit into themselves, creating very impressivegeometric symmetries.
# 
# See a very simple example of this idea in the following figure, which shows an object that is an orthogonal profile defined by a sequence of natural numbers representing the sequence of heights. We can take a copy of the object, rotate it 180 degrees and fit it perfectly into the original object, forming a rectangle.
# 
# 
# 
# In more general terms, if a sequence of N natural numbers representing the sequence of heights is A1, A2, A3, ..., AN-2, AN-1, AN, the profile defined will be called an Escher profile if we have A1+ANequal to A2+AN-1equal to A3+AN-2, and so on. In this problem, you will be given the sequence of heights that define the profile and your program must decide whether the profile is Escher or not.
# 
# Input:Listof integers(int)
# 
# Output:Boolean value(bool).
# 
# 
# END_DESC

def is_figure(data: list[int]) -> bool:
    # your code here
    return False


print("Example:")
print(is_figure([1, 2, 1, 2]))

# These "asserts" are used for self-checking
assert is_figure([1, 2, 1, 2]) == True
assert is_figure([1, 3, 2, 1, 3]) == True
assert is_figure([1, 2, 2, 1]) == False
assert is_figure([4, 4, 4, 4, 4, 4, 4, 4, 4]) == True

print("The mission is done! Click 'Check Solution' to earn rewards!")