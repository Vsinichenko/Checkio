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

def ext_plus_name(s:str):
    
    if "." not in s:
        name = s
        ext = " "

    ext = s.split(".")[-1]
    name = ".".join(s.split(".")[:-1])


    if "."+ ext == s: # file has no extension
        ext=" "
        name=s

    if s.endswith("."): # file has no extension
        name = s
        ext=" "

    return ext+name


print(ext_plus_name(".bat"))


def sort_by_ext(files: list[str]) -> list[str]:
    # your code here
    files.sort(key=ext_plus_name)
    return files



# These "asserts" are used for self-checking
assert sort_by_ext(["1.cad", "1.bat", "1.aa"]) == ["1.aa", "1.bat", "1.cad"]
assert sort_by_ext(["1.cad", "1.bat", "1.aa", "2.bat"]) == [
    "1.aa",
    "1.bat",
    "2.bat",
    "1.cad",
]
print(sort_by_ext(["1.cad", "1.bat", "1.aa", ".bat"]))

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

print("Tricky example:")
#print(sort_by_ext(["1.cad", "1.bat", "1.aa"]))

tricky_case=['.config', 'my.doc', '1.exe', '345.bin', 'green.bat', 'format.c', 'no.name.', 'best.test.exe']

for el in tricky_case:
    print(el)
    print(ext_plus_name(el))
    print()

print(sort_by_ext(tricky_case))
assert sort_by_ext(tricky_case) == ['.config', 'no.name.', 'green.bat', '345.bin', 'format.c', 'my.doc', '1.exe', 'best.test.exe']


print("The mission is done! Click 'Check Solution' to earn rewards!")