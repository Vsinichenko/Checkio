#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run right-to-left

# "For centuries, left-handers have suffered unfair discrimination in a world designed for right-handers."
# Santrock, John W. (2008). Motor, Sensory, and Perceptual Development.
# 
# "Most humans (say 70 percent to 95 percent) are right-handed, a minority (say 5 percent to 30 percent)        are left-handed, and an indeterminate number of people are probably best described as ambidextrous."
# Scientific American. www.scientificamerican.com
# 
# One of the robots is charged with a simple task:    to join a sequence of strings into one sentence to produce instructions    on how to get around the ship.    But this robot is left-handed and has a tendency to joke around and confuse its right-handed friends.
# 
# You are given a sequence of strings.    You should join these strings into a chunk of text where the initial strings are separated by commas.    As a joke on the right handed robots, you should replace all cases of the words "right" with the word "left",    even if it's a part of another word. All strings are given in lowercase.
# 
# 
# 
# Input:A sequence of strings(str).
# 
# Output:The text as a comma-separated string(str).
# 
# Precondition:
# 0 < len(phrases) < 42
# 
# 
# 
# END_DESC

def left_join(phrases: tuple[str, ...]) -> str:
    turned_phrases = [phrase.replace("right", "left") for phrase in phrases]
    return ",".join(turned_phrases)


print("Example:")
print(left_join(("left", "right", "left", "stop")))

# These "asserts" are used for self-checking
assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop"
assert left_join(("bright aright", "ok")) == "bleft aleft,ok"
assert left_join(("brightness wright",)) == "bleftness wleft"
assert left_join(("enough", "jokes")) == "enough,jokes"

print("The mission is done! Click 'Check Solution' to earn rewards!")