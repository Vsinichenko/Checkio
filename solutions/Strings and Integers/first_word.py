#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run first-word

# You might see a simplified version of this mission alreadyFirst Word (simplified). This mission is a little bit more complex as not only English letters can be in the given string.
# 
# You are given a string where you have to find its first word.
# 
# When solving a task pay attention to the following points:
# 
# There can be dots and commas in a string.A string can start with a letter or, for example, one/multiple dot(s) or space(s).A word can contain an apostrophe and it's a part of a word.The whole text can be represented with one word and that's it.
# 
# Input:A string(str).
# 
# Output:A string(str).
# 
# Precondition:the text can contain a-z A-Z , . '
# 
# 
# END_DESC

def first_word(text: str) -> str:
    # your code here
    return ""


print("Example:")
print(first_word("Hello world"))

# These "asserts" are used for self-checking
assert first_word("Hello world") == "Hello"
assert first_word(" a word ") == "a"
assert first_word("don't touch it") == "don't"
assert first_word("greetings, friends") == "greetings"
assert first_word("... and so on ...") == "and"
assert first_word("hi") == "hi"

print("The mission is done! Click 'Check Solution' to earn rewards!")