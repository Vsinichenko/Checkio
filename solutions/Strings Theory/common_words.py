#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run common-words

# Let's continue examining words. You are given two strings with words separated by commas.    Try to find what is common between these strings. The words in the same string don't repeat.
# 
# Your function should find all of the words that appear in both strings.    The result must be represented as a string of words separated by commas inalphabetic order.
# 
# Input:Two arguments as strings(str).
# 
# Output:The common words as a string(str).
# 
# Preconditions:Each string contains no more than 10 words;All words are separated by commas;All words consist of lowercase latin letters.
# 
# 
# END_DESC

def checkio(line1: str, line2: str) -> str:
    # your code here
    return ""


print("Example:")
print(checkio("hello,world", "hello,earth"))

# These "asserts" are used for self-checking
assert checkio("hello,world", "hello,earth") == "hello"
assert checkio("one,two,three", "four,five,six") == ""
assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two"

print("The mission is done! Click 'Check Solution' to earn rewards!")