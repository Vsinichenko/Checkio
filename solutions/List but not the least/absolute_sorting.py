#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run absolute-sorting

# Let's try some sorting. Here is sequence with the specific rules.
# 
# The sequence has various numbers. You should sort it, but sort it by absolute value in ascending order. For example, the sequence (-20, -5, 10, 15) will be sorted like so: (-5, 10, 15, -20). Your function should return the sortedlistortuple.
# 
# 
# 
# Input:Listof integers(int).
# 
# Output:Sortedlistof integers(int).
# 
# Addition:The results of your function will be shown aslistin the tests explanation panel.
# 
# Preconditions:len(set(abs(x) for x in array)) == len(array)
# 0 < len(array) < 100
# all(isinstance(x, int) for x in array)
# all(-100 < x < 100 for x in array)
# 
# 
# 
# END_DESC

def checkio(values: list) -> list:
    # your code here
    return []


print("Example:")
print(checkio([-20, -5, 10, 15]))

# These "asserts" are used for self-checking
assert checkio([-20, -5, 10, 15]) == [-5, 10, 15, -20]
assert checkio([1, 2, 3, 0]) == [0, 1, 2, 3]
assert checkio([-1, -2, -3, 0]) == [0, -1, -2, -3]

print("The mission is done! Click 'Check Solution' to earn rewards!")