#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run internet-plan

# John managed to get a great internet plan for his cell phone. The plan allows John to use a quota of up to X megabytes of data per month to surf the Internet. If John doesn't use all of his quota in a month, the unused megabytes are added to the next month's quota. According to the contract, John can never use more megabytes than his current quota.
# 
# In this problem, you are given the value of the monthly quota X and the number of megabytes that John used in each of the first N months of the plan. Your task is to determine how many megabytes John has left to use in month N+1.
# 
# For example, if X = 200 megabytes and John used 150 megabytes in the first month and 220 megabytes in the second month, then in the third month John has a quota of 230 megabytes (50 megabytes are carried over from the first to the second month, 30 megabytes are carried over from the second to the third month).
# 
# 
# 
# Input:Integer(int)andlistof integers.
# 
# Output:Integer(int).
# 
# 
# END_DESC

def internet_quota(X: int, used: list[int]) -> int:
    # your code here
    return 0


print("Example:")
print(internet_quota(200, [150, 220]))

# These "asserts" are used for self-checking
assert internet_quota(200, [150, 220]) == 230
assert internet_quota(100, [50, 80, 30]) == 240
assert internet_quota(150, [120]) == 180

print("The mission is done! Click 'Check Solution' to earn rewards!")