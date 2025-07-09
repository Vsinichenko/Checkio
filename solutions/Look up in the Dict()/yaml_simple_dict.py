#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run yaml-simple-dict

# Have you ever heard of such markup language asYAML?  It’s a friendly data serialization format. In fact it’s so friendly that both people and programs can read it quite well. You can play around with the standard by followingthis link.
# 
# YAML is a text, and you need to convert it into an object. But I’m not asking you to implement the entire YAML standard, we’ll implement it step by step.
# 
# The first step is the key-value conversion. The key can be any string consisting of Latin letters and numbers. The value can be a single-line string (which consists of spaces, Latin letters and numbers) or a number (int).
# 
# I’ll show some examples:
# 
# 
# name: Alex
# age: 12
# Converted into a dictionary.
# 
# 
# { 
#   "name": "Alex",
#   "age": 12
# } 
#  Note that the number automatically gets typeint.
# 
# Another example shows that the string may contain spaces.
# name: Alex Fox
# age: 12
# 
# class: 12b
# Will be converted into the next dictionary.
# 
# 
# {
#   "age": 12, 
#   "name": "Alex Fox", 
#   "class": "12b"
# }
# Pay attention to a few things. Between the string"age"and the string"class"there is an empty string that doesn’t interfere with parsing. The class starts with numbers, but has letters, which means it cannot be converted to numbers, so its type remains astr.
# 
# Input:A format string.
# 
# Output:An object (dictionary).
# 
# Precondition:YAML 1.2 is being used withJSON Schema.
# 
# 
# 
# 
# 
# 
# END_DESC

def yaml(a: str) -> dict:
    elements = a.split("\n")
    yaml_parsed = {}
    for el in elements:
        if ":" in el:
            k, v = el.split(":")
            k = k.strip()
            v=v.strip()
            try:
                v = int(v)
            except ValueError:
                pass
            yaml_parsed[k]=v


    return yaml_parsed


print("Example:")
print(
    yaml(
        """name: Alex
age: 12"""
    )
)

# These "asserts" are used for self-checking
assert yaml("name: Alex\nage: 12") == {"name": "Alex", "age": 12}
assert yaml("name: Alex Fox\nage: 12\n\nclass: 12b") == {
    "age": 12,
    "name": "Alex Fox",
    "class": "12b",
}

print("The mission is done! Click 'Check Solution' to earn rewards!")