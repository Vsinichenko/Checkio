#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run double-substring

# There are four substring missionsthat were born all in one day and you shouldn’t be needed more than one day to solve them. All of those mission can be simply solved by brute force, but is it always the best way to go? (you might not have access to all of those missions yet, but they are going to be available with more opened islands on the map).
# 
# This is the third mission of the series, and it’s the only one where you have to return not a substring but a substring length. You need to find a substring that repeats more than once in a given string. This reiteration shouldn't have overlaps. For example, in a string "abcab" the longest substring that repeats more than once is "ab", so the answer should be 2 (length of "ab")
# 
# Input:String(str).Output:Integer(int).
# 
# 
# 
# 
# 
# 
# END_DESC

def double_substring(line: str) -> int:
    # your code here
    return 0


print("Example:")
print(double_substring("aaaa"))

# These "asserts" are used for self-checking
assert double_substring("aaaa") == 2
assert double_substring("abc") == 0
assert double_substring("aghtfghkofgh") == 3

print("The mission is done! Click 'Check Solution' to earn rewards!")