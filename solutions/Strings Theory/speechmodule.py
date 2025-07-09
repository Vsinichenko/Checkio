#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run speechmodule

# Stephen's speech module is broken.    This module is responsible for his number pronunciation.    He has to click to input all of the numerical digits in a figure,    so when there are big numbers it can take him a long time.    Help the robot to speak properly and increase his number processing speed by writing a new speech module for him.    All the words in the string must be separated by exactly one space character.    Be careful with spaces - it's hard to see if you place two spaces instead one.
# 
# Input:An integer(int).
# 
# Output:A string(str).
# 
# How it is used:This concept may be useful for the speech synthesis software or automatic reports systems.    This system can also be used when writing a chatbot by assigning words or phrases numerical    values and having a system retrieve responses based on those values.
# 
# Precondition:0 < number < 1000
# 
# 
# END_DESC

FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
SECOND_TEN = [
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]
OTHER_TENS = [
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]
HUNDRED = "hundred"


def checkio(num: int) -> str:
    # replace this for solution
    return ""


print("Example:")
print(checkio(4))

# These "asserts" are used for self-checking
assert checkio(1) == "one"
assert checkio(2) == "two"
assert checkio(3) == "three"
assert checkio(4) == "four"
assert checkio(5) == "five"
assert checkio(6) == "six"
assert checkio(9) == "nine"
assert checkio(10) == "ten"
assert checkio(11) == "eleven"
assert checkio(12) == "twelve"
assert checkio(13) == "thirteen"
assert checkio(14) == "fourteen"
assert checkio(15) == "fifteen"
assert checkio(16) == "sixteen"
assert checkio(17) == "seventeen"
assert checkio(18) == "eighteen"
assert checkio(19) == "nineteen"
assert checkio(999) == "nine hundred ninety nine"
assert checkio(784) == "seven hundred eighty four"
assert checkio(777) == "seven hundred seventy seven"
assert checkio(88) == "eighty eight"
assert checkio(44) == "forty four"
assert checkio(20) == "twenty"
assert checkio(30) == "thirty"
assert checkio(40) == "forty"
assert checkio(50) == "fifty"
assert checkio(80) == "eighty"
assert checkio(90) == "ninety"
assert checkio(100) == "one hundred"
assert checkio(200) == "two hundred"
assert checkio(300) == "three hundred"
assert checkio(600) == "six hundred"
assert checkio(700) == "seven hundred"
assert checkio(900) == "nine hundred"
assert checkio(21) == "twenty one"
assert checkio(312) == "three hundred twelve"
assert checkio(302) == "three hundred two"
assert checkio(509) == "five hundred nine"
assert checkio(753) == "seven hundred fifty three"
assert checkio(940) == "nine hundred forty"
assert checkio(999) == "nine hundred ninety nine"

print("The mission is done! Click 'Check Solution' to earn rewards!")