#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run striped-words

# Our robots are always working to improve their linguistic skills.    For this mission, they research the Latin alphabet and its applications.
# 
# The alphabet contains both vowel and consonant letters (yes, we divide the letters).
# Vowels --A E I O U Y
# Consonants --B C D F G H J K L M N P Q R S T V W X Z
# 
# You are given a block of text with different words.     These words are separated by white spaces and punctuation marks.    Numbers are not considered as words in this mission (a mix of letters and digits is not a word either).    You should count the number of words (striped words) where the vowels with consonants are alternating;     words that you count cannot have two consecutive vowels or consonants.    The words consisting of a single letter are not striped -- don't count those. Casing is not significant for this mission.
# 
# Input:A text as a string(str).
# 
# Output:A quantity of striped words as an integer(int).
# 
# Preconditions:The text contains only ASCII symbols;0 < len(text) < 105.
# 
# 
# END_DESC

def checkio(line: str) -> int:
    # your code here
    return 0


print("Example:")
print(checkio("My name is ..."))

# These "asserts" are used for self-checking
assert checkio("My name is ...") == 3
assert checkio("Hello world") == 0
assert checkio("A quantity of striped words.") == 1
assert checkio("Dog,cat,mouse,bird.Human.") == 3

print("The mission is done! Click 'Check Solution' to earn rewards!")