#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run even-last

# 
# 
# You are givenlistof integers(int). You should find the sum of the elements with even indexes (0th, 2nd, 4th...). Then multiply this summed number and the final element of thelisttogether.      Don't forget that the first element has an index of 0.
# 
# For an emptylist, the result will always be 0 (zero).
# 
# 
# 
# Input:Listof integers(int).
# 
# Output:An integer(int).
# 
# Preconditions:0 ≤ len(array) ≤ 20
# all(isinstance(x, int) for x in array)
# all(-100 < x < 100 for x in array)
# 
# 
# 
# END_DESC

checkio = lambda ls: sum(ls[::2])*ls[-1] if ls else 0


print("Example:")
print(checkio([0, 1, 2, 3, 4, 5]))

# These "asserts" are used for self-checking
assert checkio([0, 1, 2, 3, 4, 5]) == 30
assert checkio([1, 3, 5]) == 30
assert checkio([6]) == 36
assert checkio([]) == 0

print("The mission is done! Click 'Check Solution' to earn rewards!")