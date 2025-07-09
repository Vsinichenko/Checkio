#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run between-markers-simplified

# You are given a string and two markers (the initial one and final). You have to find a substring enclosed between these two markers. But there are a few important conditions.
# 
# The initial and final markers are always different.The initial and final markers are always 1 char size.The initial and final markers always exist in a string and go one after another.
# 
# Input:Three arguments. All of them are strings(str). The second and third arguments are the initial and final markers.
# 
# Output:A string(str).
# 
# Precondition:There can't be more than one final and one initial markers.
# 
# 
# END_DESC

def between_markers(text: str, start: str, end: str) -> str:
    right_part = text.split(start)[-1]
    return right_part.split(end)[0]


print("Example:")
print(between_markers("What is >apple<", ">", "<"))

# These "asserts" are used for self-checking
assert between_markers("What is >apple<", ">", "<") == "apple"
assert between_markers("What is [apple]", "[", "]") == "apple"
assert between_markers("What is ><", ">", "<") == ""
assert between_markers("[an apple]", "[", "]") == "an apple"

print("The mission is done! Click 'Check Solution' to earn rewards!")