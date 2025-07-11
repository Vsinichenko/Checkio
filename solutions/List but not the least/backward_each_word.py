#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run backward-each-word

# In a given string you should reverse every word, but the words should stay in their places.
# 
# 
# 
# Input:A string(str).
# 
# Output:A string(str).
# 
# Precondition:The line consists only from alphabetical symbols and spaces.
# 
# 
# END_DESC

def backward_string_by_word(text: str) -> str:
    ls = text.split(" ")
    ls = [word[::-1] for word in ls]
    return " ".join(ls)


print("Example:")
print(backward_string_by_word(""))

# These "asserts" are used for self-checking
assert backward_string_by_word("") == ""
assert backward_string_by_word("world") == "dlrow"
assert backward_string_by_word("hello world") == "olleh dlrow"
assert backward_string_by_word("hello   world") == "olleh   dlrow"
assert backward_string_by_word("welcome to a game") == "emoclew ot a emag"

print("The mission is done! Click 'Check Solution' to earn rewards!")