#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run best-stock

# You are given the current stock prices. You have to find out which stocks cost more.
# 
# Input:The dictionary where the market identifier code is a key and the value is a stock price.
# 
# Output:The market identifier code (ticker symbol) as a string.
# 
# Preconditions:All the prices are unique.
# 
# 
# END_DESC

def best_stock(data: dict[str, float]) -> str:
    # your code here
    return ""


print("Example:")
print(best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}))

assert best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}) == "ATX"
assert best_stock({"CAC": 91.1, "ATX": 1.01, "TASI": 120.9}) == "TASI"

print("The mission is done! Click 'Check Solution' to earn rewards!")