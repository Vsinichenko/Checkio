#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run price-research

# A journalist collected data on the prices of alcohol and gasoline in several states for a report on the economic advantage of filling up with alcohol. The rule used is that alcohol is considered advantageous when its price per liter is at most 70% of the price per liter of gasoline. Given the prices collected, your program must identify in which states it is more advantageous to fill up with alcohol. If it is not advantageous to use alcohol in any state, return a list with single element"*".
# 
# 
# 
# Input:Listof tuples(tuple). Each tuple includes a string(str)and two floats(float).
# 
# Output:List of strings.
# 
# Examples:
# 
# assert filter_regions([("AM", 7.0, 10.0), ("RS", 7.01, 10.0)]) == ["AM"]
# assert filter_regions([("SP", 4.9, 5.8), ("RJ", 4.7, 5.7), ("PR", 4.6, 5.6)]) == ["*"]
# assert filter_regions(
#     [("SC", 5.2, 5.72), ("MT", 4.22, 6.1), ("AL", 5.55, 6.2), ("GO", 4.3, 6.25)]
# ) == ["MT", "GO"]
# 
# END_DESC

def filter_regions(reg: list[tuple[str, float, float]]) -> list[str]:
    # your code here
    return []


print("Example:")
print(filter_regions([("AM", 7.00, 10.00), ("RS", 7.01, 10.00)]))

# These "asserts" are used for self-checking
assert filter_regions([("AM", 7.0, 10.0), ("RS", 7.01, 10.0)]) == ["AM"]
assert filter_regions([("SP", 4.9, 5.8), ("RJ", 4.7, 5.7), ("PR", 4.6, 5.6)]) == ["*"]
assert filter_regions(
    [("SC", 5.2, 5.72), ("MT", 4.22, 6.1), ("AL", 5.55, 6.2), ("GO", 4.3, 6.25)]
) == ["MT", "GO"]

print("The mission is done! Click 'Check Solution' to earn rewards!")