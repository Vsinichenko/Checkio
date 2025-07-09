#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run bigger-price

# You have a list with all available products in a store. The data is represented as a list of dicts
# 
# Your mission here is to find the most expensive products in the list. The number of products we are looking for will be given as the first argument and the list of all products as the second argument.
# 
# Input:int and list of dicts. Each dict has the two keys "name" and "price"
# 
# Output:The same format as the second input argument.
# 
# 
# END_DESC

import pandas as pd


def bigger_price(limit: int, data: list[dict]) -> list[dict]:
    df = pd.DataFrame(data)
    df = df.sort_values(by="price", ascending=False)
    df = df.iloc[:limit]
    ret_data = df.to_dict(orient="records")
    # your code here
    return ret_data


print("Example:")
print(
    bigger_price(
        2,
        [
            {"name": "bread", "price": 100},
            {"name": "wine", "price": 138},
            {"name": "meat", "price": 15},
            {"name": "water", "price": 1},
        ],
    )
)

assert bigger_price(
    2,
    [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1},
    ],
) == [{"name": "wine", "price": 138}, {"name": "bread", "price": 100}]
assert bigger_price(
    1, [{"name": "pen", "price": 5}, {"name": "whiteboard", "price": 170}]
) == [{"name": "whiteboard", "price": 170}]

print("The mission is done! Click 'Check Solution' to earn rewards!")