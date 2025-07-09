#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run pangram

# A pangram (Greek:παν γράμμα, pan gramma, "every letter") or holoalphabetic sentence for a given alphabet is a sentence using every letter of the alphabet at least once. Perhaps you are familiar with the well known pangram"The quick brown fox jumps over the lazy dog".
# 
# 
# 
# For this mission, we will use the latin alphabet (A-Z). You are given a text with latin letters and punctuation symbols. You need to check if the sentence is a pangram or not. Case does not matter.
# 
# Input:A text as a string(str).
# 
# Output:Whether the sentence is a pangram or not as logic value(bool).
# 
# Precondition:
# 
# all(ch in (string.punctuation + string.ascii_letters + " ") for ch in text);0 < len(text).
# END_DESC

def check_pangram(text: str) -> bool:
    # your code here
    return False


print("Example:")
print(check_pangram("The quick brown fox jumps over the lazy dog."))

# These "asserts" are used for self-checking
assert check_pangram("The quick brown fox jumps over the lazy dog.") == True
assert check_pangram("ABCDEF") == False
assert check_pangram("abcdefghijklmnopqrstuvwxyz") == True
assert check_pangram("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == True
assert check_pangram("abcdefghijklmnopqrstuvwxy") == False
assert (
    check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!")
    == True
)
assert check_pangram("As quirky joke, chefs won't pay devil magic zebra tax.") == True
assert check_pangram("Six big devils from Japan quickly forgot how to walt.") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")