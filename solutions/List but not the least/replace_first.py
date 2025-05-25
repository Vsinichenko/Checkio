#!/usr/bin/env checkio --domain=py run replace-first

# 
# 
# In a given sequence the first element should become the last one. An empty sequence or with only one element should stay the same.
# 
# 
# 
# Input:List.
# 
# Output:Listor anotherIterable(tuple,iterator,generator).
# 
# 
# END_DESC

def replace_first(items: list):
    if not items or len(items) ==1:
        return items
    else:
        ls = items[1:] 
        ls.append(items[0])
        return ls
          
def replace_first(items: list) -> list:
    return items[1:] + items[:1] # slicing does not throw error for empty string

        

# These "asserts" are used for self-checking
print("Example:")
print(list(replace_first([1, 2, 3, 4])))

assert replace_first([1, 2, 3, 4]) == [2, 3, 4, 1]
assert replace_first([1]) == [1]
assert replace_first([]) == []

print("The mission is done! Click 'Check Solution' to earn rewards!")