#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run cryptarithmetic-puzzle

# This is a mission to create a solver for thecryptarithmetic  puzzle.In this puzzle, each letter must be assigned a one-digit number to complete the calculation.
# 
# You are given a list of words.The last word is the sum.You have to return a dictionary with the alphabets as keys and the one-digit numbers as values.
# 
# NOTE:Each letter should represent a different digit.The leading digit of a multi-digit number must not be zero.All tests always have one answer.
# 
# Examples:
# 
# 
# 
# 
# assert cryptarithm_solver(['SEND', 'MORE', 'MONEY']) == {'S': 9, 'E': 5, 'N': 6, 'D': 7, 'M': 1, 'O': 0, 'R': 8, 'Y': 2}
# assert cryptarithm_solver(['SIX', 'SEVEN', 'SEVEN', 'TWENTY']) == {'Y': 4, 'X': 0, 'N': 2, 'I': 5, 'E': 8, 'T': 1, 'S': 6, 'V': 7, 'W': 3}
# Input:The list of words (A list of string)
# 
# Output:The dictionary that the alphabets corresponds to the one-digit numbers (A dictionary)
# 
# Precondition:len(words) <= 10
# 
# 
# END_DESC

def cryptarithm_solver(words: str) -> dict[str, int]:
    # your code here
    return {}


print("Example:")
print(cryptarithm_solver(["SEND", "MORE", "MONEY"]))

# These "asserts" are used for self-checking
assert cryptarithm_solver(["SEND", "MORE", "MONEY"]) == {
    "O": 0,
    "M": 1,
    "Y": 2,
    "E": 5,
    "N": 6,
    "D": 7,
    "R": 8,
    "S": 9,
}
assert cryptarithm_solver(["BLACK", "GREEN", "ORANGE"]) == {
    "C": 0,
    "O": 1,
    "A": 2,
    "R": 3,
    "E": 4,
    "G": 5,
    "N": 6,
    "B": 7,
    "K": 8,
    "L": 9,
}
assert cryptarithm_solver(["POTATO", "TOMATO", "PUMPKIN"]) == {
    "U": 0,
    "P": 1,
    "N": 2,
    "M": 3,
    "A": 4,
    "O": 6,
    "I": 7,
    "T": 8,
    "K": 9,
}
assert cryptarithm_solver(["KYOTO", "OSAKA", "TOKYO"]) == {
    "A": 0,
    "Y": 1,
    "S": 2,
    "O": 3,
    "K": 4,
    "T": 7,
}

print("The mission is done! Click 'Check Solution' to earn rewards!")