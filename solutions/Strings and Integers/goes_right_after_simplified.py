#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run goes-right-after-simplified

# In a given string you need to check if one symbol goes right after another. If so - returnTrue, otherwise -False.
# 
# If one of the symbols is not in the given word - your function should returnFalse. If two seeking symbols are the same - your function should returnFalse.
# 
# 
# 
# Input:Three arguments. The first one is a given string(str), second is a symbol(str)that should go first, and the third is a symbol(str)that should go after the first one.
# 
# Output:A logic value(bool).
# 
# Preconditions:all symbols are lowercased and unique.
# 
# 
# END_DESC

def goes_after(word: str, first: str, second: str) -> bool:
    if first not in word or second not in word or first == second:
        return False
    first_i = word.find(first)
    try:
        if word[first_i+1]==second:
            return True
    except Exception:
        pass
    return False


print("Example:")
print(goes_after("world", "w", "o"))

# These "asserts" are used for self-checking
assert goes_after("world", "w", "o") == True
assert goes_after("world", "w", "r") == False
assert goes_after("world", "l", "o") == False
assert goes_after("list", "l", "o") == False
assert goes_after("", "l", "o") == False
assert goes_after("list", "l", "l") == False
assert goes_after("world", "d", "w") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")