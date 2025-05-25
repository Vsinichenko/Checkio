#!/usr/bin/env checkio --domain=py run number-length

# You have a non-negative integer. Try to find out how many digits it has.
# 
# 
# 
# Input:A non-negative integer(int).
# 
# Output:An integer(int).
# 
# 
# END_DESC

def number_length(value: int) -> int:
    return len(str(value))
            
        
        
        
    


print("Example:")
print(number_length(1456))
print(number_length(3))


# These "asserts" are used for self-checking
assert number_length(10) == 2
assert number_length(0) == 1
assert number_length(4) == 1
assert number_length(44) == 2

print("The mission is done! Click 'Check' to earn cool rewards!")