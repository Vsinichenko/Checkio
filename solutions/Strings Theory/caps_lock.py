#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run caps-lock

# Joe Palooka has fat fingers, so he always hits the “Caps Lock” key whenever he actually intends to hit the key “a” by itself. (When Joe tries to type in some accented version of “a” that needs more keystrokes to conjure the accents, he is more careful in the presence of such sophisticated characters ([Shift] + [a]) and will press the keys correctly.) Compute and return the result of having Joe type in the given text. The “Caps Lock” key affects only the letter keys “a” and “z”, and has no effect on the other keys or characters. The “Caps Lock” key is assumed to be initially off.
# 
# For Joe's keyboard, Caps Lock always uppercases a letter. That means if Caps Lock is on, and Joe does Shift + b, 'B' (in upper case) gets printed.
# 
# Input:A string (str). The typed text.
# 
# Output:A string (str). The resulting text after being typed.
# 
# The mission was taken from Python CCPS 109 Fall 2018. It was taught for the Ryerson Chang School of Continuing Education byIlkka Kokkarinen
# 
# 
# END_DESC

def caps_lock(text: str) -> str:
    # your code here
    return ""


print("Example:")
print(caps_lock("Why are you asking me that?"))

# These "asserts" are used for self-checking
assert caps_lock("Why are you asking me that?") == "Why RE YOU sking me thT?"
assert caps_lock("Always wanted to visit Zambia.") == "AlwYS Wnted to visit ZMBI."
assert caps_lock("Aloha from Hawaii") == "Aloh FROM HwII"

print("The mission is done! Click 'Check Solution' to earn rewards!")