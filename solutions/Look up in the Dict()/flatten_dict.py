#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run flatten-dict

# Nikola likes to categorize everything in sight.    One time Stephan gave him a label maker for his birthday,    and the robots were peeling labels off of every surface in the ship for weeks.    He has since categorized all the reagents in his laboratory,    books in the library and notes on the desk.    But then he learned about Pythondictionaries,    and categorized all the possible configurations for Sophia’s drones.    Now the files are organized in a deep nested structure,    but Sophia doesn’t like this. Let's help Sophia to flatten these dictionaries.
#
# Python dictionaries are a convenient data type to store and process configurations.    They allow you to store data by keys to create nested structures.    You are given a dictionary where the keys are strings and the values are strings or dictionaries.    The goal is flatten the dictionary, but save the structures in the keys.    The result should be the a dictionary without the nested dictionaries.    The keys should contain paths that contain the parent keys from the original dictionary.    The keys in the path are separated by a"/". If a value is an empty dictionary,    then it should be replaced by an empty string ("").
#
# Example:Result:
# {
#     "name": {
#         "first": "One",
#         "last": "Drone"
#     },
#     "job": "scout",
#     "recent": {},
#     "additional": {
#         "place": {
#             "zone": "1",
#             "cell": "2"}
#     }
# }
#
# {
#
# "name/first": "One",           # one parent
# "name/last": "Drone",
#
# "job": "scout",                # root key
# "recent": "",                  # empty dict
#
#
# "additional/place/zone": "1",  # third level
# "additional/place/cell": "2"
# }
#
#             Input:An original dictionary as a dict.
#
# Output:The flattened dictionary as a dict.
#
# Preconditions:keysin a dictionary are non-empty strings;valuesin a dictionary are strings or dicts;root_dictionary != {}.
#
#
# END_DESC


tricky_case = {
        "name": {"first": "Second", "last": "Drone", "nick": {}},
        "job": {
            "1": "scout",
            "2": "worker",
            "3": "writer",
            "4": "reader",
            "5": "learner",
        },
        "recent": {
            "places": {"earth": {"Louvre": "2015", "NY": "2017", "NP": ""}},
            "times": {"XX": {"1964": "Yes"}, "XXI": {"2064": "Nope"}},
        },
    }

from collections.abc import MutableMapping

def flatten(d: MutableMapping, parent_key: str = '', sep: str ='/') -> MutableMapping:
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, MutableMapping) and v!={}:
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            if v=={}:
                v=""
            items.append((new_key, v))
    return dict(items)


print("Example:")
print(flatten({"key": "value"}))
print(flatten(tricky_case))

val = tricky_case.values()



assert flatten(tricky_case) == {
    "job/1": "scout",
    "recent/places/earth/NY": "2017",
    "job/3": "writer",
    "job/2": "worker",
    "job/5": "learner",
    "job/4": "reader",
    "recent/places/earth/NP": "",
    "recent/places/earth/Louvre": "2015",
    "recent/times/XX/1964": "Yes",
    "recent/times/XXI/2064": "Nope",
    "name/first": "Second",
    "name/last": "Drone",
    "name/nick": "",
}


# These "asserts" are used for self-checking
assert flatten({"key": "value"}) == {"key": "value"}
assert flatten({"key": {"deeper": {"more": {"enough": "value"}}}}) == {
    "key/deeper/more/enough": "value"
}
assert flatten({"empty": {}}) == {"empty": ""}
assert flatten(
    {
        "name": {"first": "One", "last": "Drone"},
        "job": "scout",
        "recent": {},
        "additional": {"place": {"zone": "1", "cell": "2"}},
    }
) == {
    "name/first": "One",
    "name/last": "Drone",
    "job": "scout",
    "recent": "",
    "additional/place/zone": "1",
    "additional/place/cell": "2",
}


print("The mission is done! Click 'Check Solution' to earn rewards!")
