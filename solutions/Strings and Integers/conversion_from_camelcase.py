#!/usr/bin/env checkio --domain=py run conversion-from-camelcase

# Your mission is to convert the name of a function from CamelCase ("MyFunctionName") into the Python format ("my_function_name") where all chars are in lowercase and all words are concatenated with an intervening underscore symbol "_".
# 
# 
# 
# Input:A function name as a CamelCase string(str).
# 
# Output:The same string(str), but in under_score.
# 
# Precondition:
# 0 < len(string) <= 100
# Input data won't contain any numbers.
# 
# 
# 
# END_DESC

def from_camel_case(name: str) -> str:
    # replace this for solution
    return ""


print("Example:")
print(from_camel_case("MyFunctionName"))

# These "asserts" are used for self-checking
assert from_camel_case("MyFunctionName") == "my_function_name"
assert from_camel_case("IPhone") == "i_phone"

print("The mission is done! Click 'Check Solution' to earn rewards!")