#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run brackets

# “Great!” Exclaimed Sofia. “Now we have the password.”
# 
# “To what exactly?” Quipped Nikola.
# 
# “Untold treasures, vast riches beyond belief! Gold! Silver! Silicon! Hydraulic Fluid! Anything your heart        desires!”
# 
# “And you’re going to do what with a password to absolutely nothing?” Nikola smirked.
# 
# “Oh... Right...”
# 
# Stephen spoke up. “Well, this door back here has a keypad. Only thing is the brackets look pretty busted up. We        could try fixing it and then punching in the password?”
# 
# “YES! That!” Sofia exclaimed.
# 
# You are given an expression with numbers, brackets and operators.    For this task only the brackets matter. Brackets come in three flavors: "{}" "()" or "[]".    Brackets are used to determine scope or to restrict some expression.    If a bracket is open, then it must be closed with a closing bracket of the same type.    The scope of a bracket must not intersected by another bracket.    In this task you should make a decision, whether to correct an expression or not based on the brackets.    Do not worry about operators and operands.
# 
# Input:An expression with different of types brackets as a string(str).
# 
# Output:A verdict on the correctness of the expression as logic value(bool).
# 
# Preconditions:There are only brackets ("{}" "()" or "[]"), digits or operators ("+" "-" "*" "/");0 < len(expression) < 103.
# 
# 
# END_DESC

def checkio(expression: str) -> bool:
    # your code here
    return False


# These "asserts" using only for self-checking and not necessary for auto-testing

print("Example:")
print(checkio("((5+3)*2+1)"))

# These "asserts" are used for self-checking
assert checkio("((5+3)*2+1)") == True
assert checkio("{[(3+1)+2]+}") == True
assert checkio("(3+{1-1)}") == False
assert checkio("[1+1]+(2*2)-{3/3}") == True
assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False
assert checkio("[(3)+(-1)]*{3}") == True
assert checkio("(((([[[{{{3}}}]]]]))))") == False
assert checkio("[1+202]*3*({4+3)}") == False
assert checkio("({[3]})-[4/(3*{1001-1000}*3)/4]") == True
assert checkio("[[[1+[1+1]]])") == False
assert checkio("(((1+(1+1))))]") == False
assert checkio("2+3") == True

print("The mission is done! Click 'Check Solution' to earn rewards!")