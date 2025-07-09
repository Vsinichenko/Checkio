#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run backward-string

# You should return a given string in reverse order.
# 
# 
# 
# Input:A string(str).
# 
# Output:A string(str).
# 
# 
# END_DESC

def backward_string(val: str) -> str:
    res = ""
    for i, letter in enumerate(list(val)):
        need_i = len(val)-(i+1)
        res = res + val[need_i]
    return res
        


print("Example:")
print(backward_string("val"))

# These "asserts" are used for self-checking
assert backward_string("val") == "lav"
assert backward_string("") == ""
assert backward_string("ohho") == "ohho"
assert backward_string("123456789") == "987654321"

print("The mission is done! Click 'Check Solution' to earn rewards!")