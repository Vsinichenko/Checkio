#!/usr/bin/env checkio --domain=py run conversion-into-camelcase

# Your mission is to convert the name of a function from the Python format (for example "my_function_name") intoCamelCase("MyFunctionName") where the first char of every word is in uppercase and all words are concatenated without any intervening characters.
# 
# 
# 
# Input:A function name as a string(str).
# 
# Output:The same string(str), but in CamelCase.
# 
# Precondition:
# 0 < len(string) <= 100
# Input data won't contain any numbers.
# 
# 
# 
# END_DESC

def to_camel_case(name: str) -> str:
    # replace this for solution
    return ""


print("Example:")
print(to_camel_case("my_function_name"))

# These "asserts" are used for self-checking
assert to_camel_case("my_function_name") == "MyFunctionName"
assert to_camel_case("i_phone") == "IPhone"

print("The mission is done! Click 'Check Solution' to earn rewards!")