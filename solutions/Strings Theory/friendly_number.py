#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run friendly-number

# Long numbers can be made to look nicer, so let’s write some code to do just that.
# 
# You should write a function for converting anumberto string using several rules.
# 
# First of all, you will need to cut the number with a given base (baseargument; default 1000).
# 
# The value is a float number with decimal after the point (decimalsargument; default 0).    For the value, use the rounding towards zero rule (5.6 ⇒ 5, -5.6 ⇒ -5, to integer part) if the decimal = 0,    otherwise use the standard rounding procedure.
# 
# If the number of decimals is greater than the current number of digits after dot, trail value with zeroes.
# 
# The number should be a value with letters designating the power.    You will be given a list of power designations (powersargument; default["", "k", "M", "G", "T", "P", "E", "Z", "Y"]). If you don’t have enough powers - stay at the maximum.
# 
# If you are given suffix (suffixargument; default""), then you must append it.
# 
# And zero is always zero without powers, but with suffix.
# 
# Let's look at examples. It will be simpler.
# 
# NumberResultExplanation102"102"the base is default 1000 and 102 is lower this base10240"10k"the base is default 1000 and rounding down12341234, decimals=1"12.3M"one digit after the dot12000000, decimals=3"12.000M"trailing zeros12461, decimals=1"12.5k"standard rounding1024000000, base=1024, suffix="iB""976MiB"the different base and the suffix-150, base=100, powers=["", "d", "D"]"-1d"the negative number and rounding towards zero-155, base=100, decimals=1, powers=["", "d", "D"]"-1.6d"the negative number and standard rounding255000000000, powers=["", "k", "M"]"255000M"there is not enough powersInput:number, base, decimalsas integers(int),suffixas a string(str),powersaslistof strings(str).
# 
# Output:The converted number as a string(str).
# 
# How it is used:In the physics and IT we have a lot of various numbers.    Sometimes we need to make them more simpler and easier to read. When you talk about gigabytes sometimes you don’t need to know the exact number bytes or kilobytes.
# 
# Preconditions:1 < base ≤ 1032-1032< number ≤ 10320 ≤ decimals ≤ 150 < len(powers) ≤ 32
# 
# 
# END_DESC

def friendly_number(number: int, options: dict) -> str:
    # your code here
    return ""


print("Example:")
print(friendly_number(102, {}))

# These "asserts" are used for self-checking
assert friendly_number(102, {}) == "102"
assert friendly_number(12341234, {"decimals": 1}) == "12.3M"
assert friendly_number(12000000, {"decimals": 3}) == "12.000M"
assert friendly_number(102, {"decimals": 2}) == "102.00"
assert friendly_number(10240, {}) == "10k"
assert friendly_number(1024000000, {"base": 1024, "suffix": "iB"}) == "976MiB"
assert friendly_number(-150, {"base": 100, "powers": ["", "d", "D"]}) == "-1d"
assert (
    friendly_number(-155, {"base": 100, "decimals": 1, "powers": ["", "d", "D"]})
    == "-1.6d"
)
assert friendly_number(255000000000, {"powers": ["", "k", "M"]}) == "255000M"

print("The mission is done! Click 'Check Solution' to earn rewards!")