#!/usr/bin/env checkio --domain=py run zigzag-array

# Your function should create alistoflists, that represents a two-dimensional grid with the given number of rows and cols.
# 
# This grid should contain integers(int)fromstarttostart + rows * cols - 1in ascending order, but the elements of every odd-index row have to be listed in descending order, so that when read in ascending order, the numbers zigzag through the two-dimensional grid.
# 
# 
# 
# Input:Two integers(int)- rows and columns. One optional integer(int)- start.
# 
# Output:Listoflists.
# 
# The mission was taken from Python CCPS 109 Fall 2018. It is taught for Ryerson Chang School of Continuing Education byIlkka Kokkarinen
# 
# 
# END_DESC

def create_zigzag(rows: int, cols: int, start: int = 1) -> list[list[int]]:
    # your code here
    return [[]]


print("Example:")
print(create_zigzag(3, 5))

# These "asserts" are used for self-checking
assert create_zigzag(3, 5) == [[1, 2, 3, 4, 5], [10, 9, 8, 7, 6], [11, 12, 13, 14, 15]]
assert create_zigzag(5, 1) == [[1], [2], [3], [4], [5]]
assert create_zigzag(3, 3, 5) == [[5, 6, 7], [10, 9, 8], [11, 12, 13]]

print("The mission is done! Click 'Check Solution' to earn rewards!")