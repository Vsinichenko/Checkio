#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run popular-words

# In this mission your task is to determine the popularity of certain words in the text.
# 
# At the input of your function are given 2 arguments: the text and the array of words the popularity of which you need to determine.
# 
# When solving this task pay attention to the following points:
# 
# The words should be sought in all registers. This means that if you need to find a word "one" then words like "one", "One", "oNe", "ONE" etc. will do.The search words are always indicated in the lowercase.If the word wasn’t found even once, it has to be returned in the dictionary with  0 (zero) value.Input:The text and the search words array.
# 
# Output:The dictionary where the search words are the keys and values are the number of times when those words are occurring in a given text.
# 
# Precondition:
# The input text will consists of English letters in uppercase and lowercase and whitespaces.
# 
# 
# END_DESC

def popular_words(text: str, words: list) -> dict:
    # your code here
    return {}


print("Example:")
print(
    popular_words(
        """
When I was One
I had just begun
When I was Two
I was nearly new
""",
        ["i", "was", "three", "near"],
    )
)

assert popular_words(
    "\nWhen I was One\nI had just begun\nWhen I was Two\nI was nearly new\n",
    ["i", "was", "three", "near"],
) == {"i": 4, "was": 3, "three": 0, "near": 0}

print("The mission is done! Click 'Check Solution' to earn rewards!")