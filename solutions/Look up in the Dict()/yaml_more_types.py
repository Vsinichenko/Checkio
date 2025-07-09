#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run yaml-more-types

# This is the second task on parsing YAML. It represents the next step where parsing gets more complicated. The data types, such asNoneandbool, are being added, and besides that, you’re getting the ability to use quotes in strings.
# 
# Here are some of the examples:
# 
# 
# name: "Bob Dylan"
# children: 6
# 
# {
#   "name": "Bob Dylan", 
#   "children": 6
# }      
#       
# name: "Alex \\"Fox\\""
# children: 6
# 
# {
#   "name": "Alex \"Fox\"",
#   "children": 6
# }           
#       As you can see, the string can be put in quotes. It can be both double and single quotes.
# 
# 
# name: "Bob Dylan"
# children: 6
# alive: false
#         
# {
#   "name": "Bob Dylan", 
#   "alive": False, 
#   "children": 6
# }    
#       TrueandFalseare the keywords defining the bool type.
# 
# 
# name: "Bob Dylan"
# children: 6
# coding:
#         
# {
#   "coding": None, 
#   "name": "Bob Dylan", 
#   "children": 6
# }
#       If no value is specified, it becomes undefined. There also is a keyword for this -None.
# 
# Input:A format string.
# 
# Output:An object (list/dictionary).
# 
# Precondition:YAML 1.2 is being used withJSON Schema.
# 
# 
# END_DESC

# Taken from mission YAML. Simple Dict

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
    yaml(
        """name: Alex
age: 12"""
    )
)
    "age": 12,
    "name": "Alex Fox",
    "class": "12b",
}


print("Example:")
print(yaml("name: Alex\nage: 12"))

# These "asserts" are used for self-checking
assert yaml("name: Alex\nage: 12") == {"name": "Alex", "age": 12}
assert yaml("name: Alex Fox\nage: 12\n\nclass: 12b") == {
    "name": "Alex Fox",
    "age": 12,
    "class": "12b",
}
assert yaml('name: "Alex Fox"\nage: 12\n\nclass: 12b') == {
    "name": "Alex Fox",
    "age": 12,
    "class": "12b",
}
assert yaml('name: "Alex \\"Fox\\""\nage: 12\n\nclass: 12b') == {
    "name": 'Alex "Fox"',
    "age": 12,
    "class": "12b",
}
assert yaml('name: "Bob Dylan"\nchildren: 6\nalive: false') == {
    "name": "Bob Dylan",
    "children": 6,
    "alive": False,
}
assert yaml('name: "Bob Dylan"\nchildren: 6\ncoding:') == {
    "name": "Bob Dylan",
    "children": 6,
    "coding": None,
}
assert yaml('name: "Bob Dylan"\nchildren: 6\ncoding: null') == {
    "name": "Bob Dylan",
    "children": 6,
    "coding": None,
}
assert yaml('name: "Bob Dylan"\nchildren: 6\ncoding: "null" ') == {
    "name": "Bob Dylan",
    "children": 6,
    "coding": "null",
}

print("The mission is done! Click 'Check Solution' to earn rewards!")