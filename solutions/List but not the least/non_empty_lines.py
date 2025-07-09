#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run non-empty-lines

# You need to count how many non-empty lines a given text has.
# 
# An empty line is a line without symbols or the one that contains only spaces.
# 
# 
# 
# Input:A text(str).
# 
# Output:An integer(int).
# 
# 
# END_DESC

def non_empty_lines(text: str) -> int:
    # your code here
    return 0


print("Example:")
print(non_empty_lines("one simple line\n"))

# These "asserts" are used for self-checking
assert non_empty_lines("one simple line\n") == 1
assert non_empty_lines("") == 0
assert non_empty_lines("\nonly one line\n            ") == 1
assert (
    non_empty_lines(
        "\nLorem ipsum dolor sit amet,\n\nconsectetur adipiscing elit\nNam odio nisi, aliquam\n            "
    )
    == 3
)

print("The mission is done! Click 'Check Solution' to earn rewards!")