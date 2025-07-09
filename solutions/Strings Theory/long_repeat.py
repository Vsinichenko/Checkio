#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run long-repeat

# There are four substring missionsthat were born all in one day and you shouldn’t need more than one day to solve them. All of these missions can be simply solved by brute force, but is it always the best way to go? (You might not have access to all of those missions yet, but they are going to be available with more opened islands on the map).
# 
# This mission is the first one of the series. Here you should find the length of the longest substring that consists of the same letter. For example, line "aaabbcaaaa" contains four substrings with the same letters "aaa", "bb","c" and "aaaa". The last substring is the longest one, which makes it the answer.
# 
# Input:A string.Output:An int.
# 
# 
# 
# 
# 
# 
# END_DESC

def long_repeat(line: str) -> int:
    """
    length the longest substring that consists of the same char
    """
    # your code here
    return 0


print("Example:")
print(long_repeat("sdsffffse"))

assert long_repeat("sdsffffse") == 4
assert long_repeat("ddvvrwwwrggg") == 3

print("The mission is done! Click 'Check Solution' to earn rewards!")