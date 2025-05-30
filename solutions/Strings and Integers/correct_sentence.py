#!/home/valentyna-sinichenko/miniconda3/bin/checkio --domain=py run correct-sentence

# For the input of your function, you will be given one sentence. You have to return a corrected version, that starts with a capital letter and ends with a period (dot).
# 
# Pay attention to the fact that not all of the fixes are necessary. If a sentence already ends with a period (dot), then adding another one will be a mistake.
# 
# 
# 
# Input:A string(str).
# 
# Output:A string(str).
# 
# Precondition:No leading and trailing spaces, text contains only spaces, a-z, A-Z, "," and ".".
# 
# 
# END_DESC

def correct_sentence(text: str) -> str:
    # your code here
    return ""


print("Example:")
print(correct_sentence("greetings, friends"))

# These "asserts" are used for self-checking
assert correct_sentence("greetings, friends") == "Greetings, friends."
assert correct_sentence("Greetings, friends") == "Greetings, friends."
assert correct_sentence("Greetings, friends.") == "Greetings, friends."
assert correct_sentence("greetings, friends.") == "Greetings, friends."

print("The mission is done! Click 'Check Solution' to earn rewards!")