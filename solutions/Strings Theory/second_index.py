#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run second-index

# You are given two strings and you have to find an index of the second occurrence of the second string in the first one.
# 
# Let's go through the first example where you need to find the second occurrence of "s" in a word "sims". It’s easy to find its first occurrence with a functionindexorfindwhich will point out that "s" is the first symbol in a word "sims" and therefore the index of the first occurrence is 0. But we have to find the second "s" which is 4th in a row and that means that the index of the second occurrence (and the answer to a question) is 3.
# 
# Input:Two strings(str).
# 
# Output:Integer(int)orNone.
# 
# 
# END_DESC

def second_index(text: str, symbol: str) -> int | None:
    # your code here
    return 0


print("Example:")
print(second_index("sims", "s"))

# These "asserts" are used for self-checking
assert second_index("sims", "s") == 3
assert second_index("find the river", "e") == 12
assert second_index("hi", " ") == None
assert second_index("hi mayor", " ") == None
assert second_index("hi mr Mayor", " ") == 5

print("The mission is done! Click 'Check Solution' to earn rewards!")