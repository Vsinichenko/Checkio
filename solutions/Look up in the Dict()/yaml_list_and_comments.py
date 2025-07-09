#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run yaml-list-and-comments

# In the 3rd YAML parsing task, we’re going to look into lists.
# 
# (Remember that in this mission you must take into account the conditions of previous missions. It means that your solution should work with dictionaries from a previous mission and with lists from this one).
# 
# A simple example:
# 
# 
# - write some
# - "Alex Chii"
# - 89
#             
# [
# "write some", 
# "Alex Chii", 
# 89
# ]
#             As you can see in the above example, the format for values is the same as we’ve used in the previous task for the format of values in the dictionary.
# 
# It's time to add comments to the format.
# 
# Everything indicated after the # sign should be ignored by the parser.
# 
# 
# # comment
# - write some # after
# # one more
# - "Alex Chii #sir "
# - 89 #bl
#             
# [
# "write some", 
# "Alex Chii #sir ", 
# 89
# ]
#             As you may have noticed, the comments inside the string aren’t considered as comments, they are treated as part of the string, which makes sense.
# 
# Input:Format string.
# 
# Output:An object (list/dictionary).
# 
# Precondition:The YAML 1.2 standard is being used.
# 
# 
# END_DESC

# Taken from mission YAML. More Types

# Taken from mission YAML. Simple Dict
import ast 
def is_bool(s) -> bool:
    return s.lower() in ["true", "false"]
def yaml(a: str) -> dict:
    elements = a.split("\n")
    yaml_parsed = {}
    for el in elements:
        if ":" in el:
            k, v = el.split(":")
            k = k.strip()
            v=v.strip()
            if v.startswith('"') and v.endswith('"'):
                v = ast.literal_eval(v)
            elif v.isdigit():
                v = int(v)
            elif v=="":
                v=None
            elif v=="null":
                v=None
            elif v =="true":
                v=True
            elif v=="false":
                v=False
            yaml_parsed[k]=v
    return yaml_parsed
    
    "name": "Alex Fox",
    "age": 12,
    "class": "12b",
}
    "name": "Alex Fox",
    "age": 12,
    "class": "12b",
}
    "name": 'Alex "Fox"',
    "age": 12,
    "class": "12b",
}
    "name": "Bob Dylan",
    "children": 6,
    "alive": False,
}
    "name": "Bob Dylan",
    "children": 6,
    "coding": None,
}
    "name": "Bob Dylan",
    "children": 6,
    "coding": None,
}
    "name": "Bob Dylan",
    "children": 6,
    "coding": "null",
}


print("Example:")
print(yaml('- write some\n- "Alex Chii"\n- 89'))

# These "asserts" are used for self-checking
assert yaml('- write some\n- "Alex Chii"\n- 89') == ["write some", "Alex Chii", 89]
assert yaml(
    '# comment\n- write some # after\n# one mor\n- "Alex Chii #sir "\n- 89 #bl'
) == ["write some", "Alex Chii #sir ", 89]
assert yaml("- 1\n- 2\n- 3\n\n- 4\n\n\n\n- 5") == [1, 2, 3, 4, 5]
assert yaml("-\n-\n-\n- 7") == [None, None, None, 7]

print("The mission is done! Click 'Check Solution' to earn rewards!")