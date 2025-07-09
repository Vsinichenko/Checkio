#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run sort-by-extension

# You are given a sequence of files as strings. You need to sort this the sequence by the file extension. The files with the same extension (or without one) should be sorted by name.
# 
# Some possible cases:
# 
# Filename cannot be an empty string;Sorting order: files without name, files without extension, files with name and extension;Filename.configorconfig.is all name with an empty extension;Filename likestr1.str2.str3has an extensionstr3and a namestr1.str2;Filename like.str1.str2has an extensionstr2and a name.str1.
# 
# Input:Listof strings(str).
# 
# Output:Listof strings(str).
# 
# 
# END_DESC

def sort_by_ext(files: list[str]) -> list[str]:
    # your code here
    return []


print("Example:")
print(sort_by_ext(["1.cad", "1.bat", "1.aa"]))

# These "asserts" are used for self-checking
assert sort_by_ext(["1.cad", "1.bat", "1.aa"]) == ["1.aa", "1.bat", "1.cad"]
assert sort_by_ext(["1.cad", "1.bat", "1.aa", "2.bat"]) == [
    "1.aa",
    "1.bat",
    "2.bat",
    "1.cad",
]
assert sort_by_ext(["1.cad", "1.bat", "1.aa", ".bat"]) == [
    ".bat",
    "1.aa",
    "1.bat",
    "1.cad",
]
assert sort_by_ext(["1.cad", "1.bat", ".aa", ".bat"]) == [
    ".aa",
    ".bat",
    "1.bat",
    "1.cad",
]
assert sort_by_ext(["1.cad", "1.", "1.aa"]) == ["1.", "1.aa", "1.cad"]
assert sort_by_ext(["1.cad", "1.bat", "1.aa", "1.aa.doc"]) == [
    "1.aa",
    "1.bat",
    "1.cad",
    "1.aa.doc",
]
assert sort_by_ext(["1.cad", "1.bat", "1.aa", ".aa.doc"]) == [
    "1.aa",
    "1.bat",
    "1.cad",
    ".aa.doc",
]

print("The mission is done! Click 'Check Solution' to earn rewards!")