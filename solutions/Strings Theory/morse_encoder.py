#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run morse-encoder

# Your task is to encrypt the text message using theMorse code. The input text will consist of letters (in uppercase and lowercase), numbers and white spaces. There won't be any special characters ('&', '?', '#' etc.)
# You need to use 3 spaces between words and 1 space between each letter of each word.
# 
# 
# 
# Input:The secret message(str).
# 
# Output:The same message(str), but encrypted.
# 
# Preconditions:0 < len(text) < 50;Only English letters (in uppercase and lowercase), numbers and white spaces.
# 
# 
# END_DESC

MORSE = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
}


def morse_encoder(text: str) -> str:
    # your code here
    return ""


print("Example:")
print(morse_encoder("some text"))

# These "asserts" are used for self-checking
assert morse_encoder("some text") == "... --- -- .   - . -..- -"
assert (
    morse_encoder("I was born in 1990")
    == "..   .-- .- ...   -... --- .-. -.   .. -.   .---- ----. ----. -----"
)

print("The mission is done! Click 'Check Solution' to earn rewards!")