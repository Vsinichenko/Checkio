#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run text-formatting

# You are given a long line (a monospace font), and you have to break the line in order to respect a given width. Then you have to format the text according to the given style:"l"means you have to align the text to theleft,"c"forcenter,"r"forright, and"j"means you have tojustify the text. Finally, the lines of the output shouldn’t end with a whitespace.
# 
# If you have to put 2 * n + 1 spaces around a line in order to center it, then put n spaces before, not n + 1.
# 
# The justification rules:since we can't always put the same number of spaces between words in a line, put big blocks of spaces first. For example: X---X---X--X--X--X when you have to put 12 spaces in 5 gaps: 3-3-2-2-2;don't justify the last line of a text.
# 
# You won't have to consider splitting a word into two parts because the given widths are big enough.
# 
# Input:A text(str), width(int)and style(str).
# 
# Output:The formatted text (str).
# 
# Preconditions:all(len(word) <= width for word in text.split());'\n' not in text;style in ('l', 'c', 'r', 'j');0 < len(text) <= 1000.
# 
# 
# END_DESC

def text_formatting(text: str, width: int, style: str) -> str:
    # your code here
    return ""


LINE = (
    "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iure "
    "harum suscipit aperiam aliquam ad, perferendis ex molestias "
    "reiciendis accusantium quos, tempore sunt quod veniam, eveniet "
    "et necessitatibus mollitia. Quasi, culpa."
)
print("Example:")
print(text_formatting(LINE, 38, "l"))

# These "asserts" are used for self-checking
assert (
    text_formatting(
        "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iure harum suscipit aperiam aliquam ad, perferendis ex molestias reiciendis accusantium quos, tempore sunt quod veniam, eveniet et necessitatibus mollitia. Quasi, culpa.",
        38,
        "l",
    )
    == "Lorem ipsum dolor sit amet,\nconsectetur adipisicing elit. Iure\nharum suscipit aperiam aliquam ad,\nperferendis ex molestias reiciendis\naccusantium quos, tempore sunt quod\nveniam, eveniet et necessitatibus\nmollitia. Quasi, culpa."
)
assert (
    text_formatting(
        "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iure harum suscipit aperiam aliquam ad, perferendis ex molestias reiciendis accusantium quos, tempore sunt quod veniam, eveniet et necessitatibus mollitia. Quasi, culpa.",
        30,
        "c",
    )
    == " Lorem ipsum dolor sit amet,\nconsectetur adipisicing elit.\n Iure harum suscipit aperiam\n  aliquam ad, perferendis ex\n     molestias reiciendis\naccusantium quos, tempore sunt\n   quod veniam, eveniet et\n   necessitatibus mollitia.\n        Quasi, culpa."
)
assert (
    text_formatting(
        "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iure harum suscipit aperiam aliquam ad, perferendis ex molestias reiciendis accusantium quos, tempore sunt quod veniam, eveniet et necessitatibus mollitia. Quasi, culpa.",
        50,
        "r",
    )
    == "           Lorem ipsum dolor sit amet, consectetur\n     adipisicing elit. Iure harum suscipit aperiam\n   aliquam ad, perferendis ex molestias reiciendis\n       accusantium quos, tempore sunt quod veniam,\n eveniet et necessitatibus mollitia. Quasi, culpa."
)
assert (
    text_formatting(
        "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iure harum suscipit aperiam aliquam ad, perferendis ex molestias reiciendis accusantium quos, tempore sunt quod veniam, eveniet et necessitatibus mollitia. Quasi, culpa.",
        45,
        "j",
    )
    == "Lorem   ipsum  dolor  sit  amet,  consectetur\nadipisicing elit. Iure harum suscipit aperiam\naliquam    ad,   perferendis   ex   molestias\nreiciendis  accusantium  quos,  tempore  sunt\nquod   veniam,   eveniet   et  necessitatibus\nmollitia. Quasi, culpa."
)

print("The mission is done! Click 'Check Solution' to earn rewards!")