#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run aggregate-by-operation

# This is a further development ofConvert and Aggregatemission.    You are given a list of tuples. Each tuple consists of two values: a string    and an integer.    You need to create and return a dictionary,    where keys are string values (except the first character) from input tuples. Values are aggregated integer    values from input tuples for each specific key.  Each aggregating operation must be done    according to the operation sign - the first character of string key.    Division by zero should be ignored. The resulted dictionary    should not include items with empty key or zero value.
# 
# Input:List of tuples.
# 
# Output:Dictionary.
# 
# Examples:
# 
# assert aggr_operation([("+a", 7), ("-b", 8), ("*a", 10)]) == {"a": 70, "b": -8}
# assert aggr_operation([]) == {}
# assert aggr_operation([("+a", 5), ("+a", -5), ("-a", 5), ("-a", -5)]) == {}
# assert aggr_operation([("*a", 0), ("=a", 0), ("/a", 0), ("-a", -5)]) == {"a": 5}
# 
# END_DESC

def aggr_operation(data: list[tuple[str, int]]) -> dict[str, int]:

    # your code here

    return {}


print("Example:")
print(aggr_operation([("+a", 7), ("-b", 8), ("*a", 10)]))

# These "asserts" are used for self-checking
assert aggr_operation([("+a", 7), ("-b", 8), ("*a", 10)]) == {"a": 70, "b": -8}
assert aggr_operation([]) == {}
assert aggr_operation([("+a", 5), ("+a", -5), ("-a", 5), ("-a", -5)]) == {}
assert aggr_operation([("*a", 0), ("=a", 0), ("/a", 0), ("-a", -5)]) == {"a": 5}

print("The mission is done! Click 'Check Solution' to earn rewards!")