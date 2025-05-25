#!/usr/bin/env checkio --domain=py run most-wanted-letter

# You are given a text, which contains different English letters and punctuation symbols.    You should find the most frequent letter in the text. The letter returned must be in lower case.
# While checking for the most wanted letter, casing does not matter, so for the purpose of your search,    "A" == "a".    Make sure you do not count punctuation symbols, digits and whitespaces, only letters.
# 
# 
# 
# If you havetwo or more letters with the same frequency,    then return the letter which comes first in the Latin alphabet.    For example --"one"contains "o", "n", "e" only once for each, thus we choose "e".
# 
# Input:A text for analysis as a string(str).
# 
# Output:The most frequent letter in lower case as a string(str).
# 
# Precondition:
# A text contains only ASCII symbols.
# 0 < len(text) ≤ 105
# 
# 
# END_DESC

def checkio(text: str) -> str:
    # your code here
    return ""


print("Example:")
print(checkio("Hello World!"))

# These "asserts" are used for self-checking
assert checkio("Hello World!") == "l"
assert checkio("How do you do?") == "o"
assert checkio("One") == "e"
assert checkio("Oops!") == "o"
assert checkio("AAaooo!!!!") == "a"
assert checkio("abe") == "a"

print("The mission is done! Click 'Check Solution' to earn rewards!")