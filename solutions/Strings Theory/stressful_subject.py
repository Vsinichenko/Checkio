#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run stressful-subject

# The function should recognize if a subject line is stressful.    A stressful subject line means that all letters are in uppercase, and/or the whole line ends    by at least 3 exclamation marks, and/or contains at least one of the following    “red” words: "help", "asap", "urgent". Any of those "red" words can be spelled    in different ways - "HELP", "help", "HeLp", "H!E!L!P!", "H-E-L-P", even in a    very loooong way "HHHEEEEEEEEELLP," they just can't have any other letters interspersed between them.
# 
# Input:Subject line as a string.
# 
# Output:Boolean.
# 
# Precondition:Subject can be up to 100 letters
# 
# 
# END_DESC

def is_stressful(subj: str) -> bool:
    """
    recognize stressful subject
    """
    return False


print("Example:")
print(is_stressful("Hi"))

assert is_stressful("Hi") == False
assert is_stressful("I neeed HELP") == True
assert is_stressful("I neeed HLEP") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")