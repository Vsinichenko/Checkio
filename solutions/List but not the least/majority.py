#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run majority

# 
# 
# We have alistof logic values(bool). Let's check if the majority of elements areTrue.
# 
# Some cases worth mentioning: 1) an emptylistshould returnFalse;    2) ifTrue-s andFalse-s have an equal amount, function should returnFalse.
# 
# 
# 
# Input:Alistof logic values(bool).
# 
# Output:A logic value(bool).
# 
# 
# END_DESC

def is_majority(items: list[bool]) -> bool:
    count_true = items.count(True)
    if count_true>len(items)-count_true:
        return True
    return False


print("Example:")
print(is_majority([True, True, False, True, False]))

# These "asserts" are used for self-checking
assert is_majority([True, True, False, True, False]) == True
assert is_majority([True, True, False]) == True
assert is_majority([True, True, False, False]) == False
assert is_majority([True, True, False, False, False]) == False
assert is_majority([False]) == False
assert is_majority([True]) == True
assert is_majority([]) == False

print("The mission is done! Click 'Check Solution' to earn rewards!")