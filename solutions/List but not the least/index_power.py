#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run index-power

# 
# 
# You are given alistwith positive integers(int)and an integer(int)N. You should find the N-th power of the element in thelistwith the index N. If N is outside of thelist, then return -1. Don't forget that the first element has the index 0.
# 
# Let's look at a few examples:
# -list= [1, 2, 3, 4] and N = 2, then the result is 32== 9;
# -list= [1, 2, 3] and N = 3, but N is outside of thelist, so the result is -1.
# 
# 
# 
# Input:Two arguments.Alistof integers(int)and an integer(int).
# 
# Output:The result as an integer(int).
# 
# Precondition:0 < len(array) ≤ 10
# 0 ≤ N
# all(0 ≤ x ≤ 100 for x in array)
# 
# 
# 
# END_DESC

def index_power(ar: list[int], n: int) -> int:
    try:
        return ar[n] ** n
    except IndexError:
        return -1


print("Example:")
print(index_power([1, 2, 3], 2))

# These "asserts" are used for self-checking
assert index_power([1, 2, 3, 4], 2) == 9
assert index_power([1, 3, 10, 100], 3) == 1000000
assert index_power([0, 1], 0) == 1
assert index_power([1, 2], 3) == -1

print("The mission is done! Click 'Check Solution' to earn rewards!")