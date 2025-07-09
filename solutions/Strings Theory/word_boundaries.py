#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run word-boundaries

# You are given a string (words) with some words separated by spaces and an integer (n) — index of a symbol in this string. You need to print the word (part ofwords, boundaried by spaces) that contains the symbol under this index. If no element matches this index, returnNone.
# 
# Note:Index is 0-based and refers to the position of a character in the string (including the space characters).
# 
# 
# 
# Input:An integer "n" — index of a symbol in words.A string "words" with some elements separated by spaces.Output:A single line — element containing the symbol under this index.
# 
# Examples:assert boundaries(2, "a b c") == "b"
# assert boundaries(8, "+ - * / ( ) = 0") == "("
# assert boundaries(12, "How do you do?") == "do?"
# assert boundaries(6, "This is a very strange test...") == "is"
# Preconditions:0 < n < 300 < length of elements < 30
# 
# 
# END_DESC

def boundaries(n: int, words: str) -> str | None:
    # your code here
    return ""


print("Example:")
print(boundaries(2, "a b c"))

# These "asserts" are used for self-checking
assert boundaries(2, "a b c") == "b"
assert boundaries(8, "+ - * / ( ) = 0") == "("
assert boundaries(12, "How do you do?") == "do?"
assert boundaries(6, "This is a very strange test...") == "is"
assert boundaries(0, "!!! What !!!") == "!!!"
assert boundaries(14, "test test ERROR") == "ERROR"
assert boundaries(1, "o o o!!!") == None

print("You are doing great! Now, it's time to check!")