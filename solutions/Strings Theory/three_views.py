#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run three-views

# The volume of an object almost derived from three views.
# 
# You are given three views (front, right side, top) as input values.    Each of these is a string consisting of A to Y.These letters assigned row-major order in a 5x5 grid.
# 
# You have to return the total volume of the object.
# 
# NOTE:The answer is maximum possible value.Examples:
# 
# 
# 
# 
# assert three_views('BCDGHILMNQRSVWX', 'CHMRW', 'LMN') == 15
# assert three_views('GHILMNQRS', 'GHILMNQRS', 'GHILMNQRS', ) == 27
# Input:The three views (front, right-side, top) (3 strings)
# 
# Output:The total volume of objects (An integer)
# 
# 
# END_DESC

def three_views(front_view: str, right_view: str, top_view: str) -> int:
    # your code here
    return 0


print("Example:")
print(three_views("BCDGHILMNQRSVWX", "CHMRW", "LMN"))

# These "asserts" are used for self-checking
assert three_views("BCDGHILMNQRSVWX", "CHMRW", "LMN") == 15
assert three_views("GHILMNQRS", "GHILMNQRS", "GHILMNQRS") == 27
assert three_views("GIMQS", "GIMQS", "GIMQS") == 9
assert (
    three_views("AFGKLMPQRSUVWXY", "AFGKLMPQRSUVWXY", "ABCDEFGHIJKLMNOPQRSTUVWXY") == 55
)

print("The mission is done! Click 'Check Solution' to earn rewards!")