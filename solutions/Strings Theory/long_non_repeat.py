#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run long-non-repeat

# There are four substring missionsthat were born all in one day and you shouldn’t need more than one day to solve them. All of those mission    can be simply solved by brute force, but is it always the best way to go? (you might not have access to all of those    missions yet, but they are going to be available with more opened islands on the map).
# 
# A very similar to the first is the second mission of the series with only one distinction is that you should look in a completely different way. You need to find the first longest substring with all unique letters. For example, in substring "abca" we have two substrings with unique letters "abc" and "bca", but we should take the first one, so the answer is "abc".
# 
# Input:String(str).Output:String(str).
# 
# 
# 
# 
# 
# 
# END_DESC

def non_repeat(line: str) -> str:
    # your code here
    return ""


print("Example:")
print(non_repeat("aaaaa"))

# These "asserts" are used for self-checking
assert non_repeat("aaaaa") == "a"
assert non_repeat("abdjwawk") == "abdjw"
assert non_repeat("abcabcffab") == "abcf"

print("The mission is done! Click 'Check Solution' to earn rewards!")