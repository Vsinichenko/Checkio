#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run the-longest-palindromic

# Write a function that finds the longestpalindromicsubstring of a given string. Try to be as efficient as possible!
# 
# If you find more than one substring, you should return the one that’s closer to the beginning.
# 
# Input:A text as a string.
# 
# Output:The longest palindromic substring.
# 
# Precondition:1 < |text| ≤ 20
# The text contains only ASCII characters.
# 
# 
# END_DESC

def longest_palindromic(a: str) -> str:
    # your code here
    return ""


print("Example:")
print(longest_palindromic("abc"))

# These "asserts" are used for self-checking
assert longest_palindromic("abc") == "a"
assert longest_palindromic("abacada") == "aba"
assert longest_palindromic("artrartrt") == "rtrartr"
assert longest_palindromic("aaaaa") == "aaaaa"

print("The mission is done! Click 'Check Solution' to earn rewards!")