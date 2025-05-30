#!/home/valentyna-sinichenko/miniconda3/bin/checkio --domain=py run verify-anagrams

# An anagram is a type of word play,    the result of rearranging the letters of a word or phrase to produce a new word or phrase,    using all the original letters exactly once.    Two words are anagrams to each other if we can get one from another by rearranging the letters.    Anagrams are case-insensitive and don't take account whitespaces.    For example: "Gram Ring Mop" and "Programming" are anagrams. But "Hello" and "Ole Oh" are not.
# 
# You are given two words or phrase. Try to verify are they anagrams or not.
# 
# Input:Two arguments as strings.
# 
# Output:Are they anagrams or not as boolean (True or False)
# 
# Preconditions:0 < |first_word| < 100;0 < |second_word| < 100;Words contain only ASCII latin letters and whitespaces.
# 
# 
# END_DESC

def verify_anagrams(a: str, b: str) -> bool:
    # your code here
    return False


print("Example:")
print(verify_anagrams("Programming", "Gram Ring Mop"))

assert verify_anagrams("Programming", "Gram Ring Mop") == True
assert verify_anagrams("Hello", "Ole Oh") == False
assert verify_anagrams("Kyoto", "Tokyo") == True

print("The mission is done! Click 'Check Solution' to earn rewards!")