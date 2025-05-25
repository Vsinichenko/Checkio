#!/usr/bin/env checkio --domain=py run sum-numbers

# In a given text you need to sum the numbers while excluding any digits that form part of a word.
# 
# The text consists of numbers, spaces and letters from the English alphabet.
# 
# 
# 
# Input:A string(str).
# 
# Output:An integer(int).
# 
# 
# END_DESC

import re

def sum_numbers(text: str) -> int:
    the_sum=0
    numbers = re.findall(r"\b\d+\b", text)
    if numbers:
        numbers = [int(n) for n in numbers]
    the_sum+=sum(numbers)
    return the_sum


print("Example:")
print(sum_numbers("hi"))

# These "asserts" are used for self-checking
assert sum_numbers("hi") == 0
assert sum_numbers("who is 1st here") == 0
assert sum_numbers("my numbers is 2") == 2
assert (
    sum_numbers(
        "This picture is an oil on canvas painting by 1st Danish artist Anna Petersen between 1845 and 1910 year"
    )
    == 3755
)
assert sum_numbers("5 plus 6 is") == 11
assert sum_numbers("") == 0

print("The mission is done! Click 'Check Solution' to earn rewards!")