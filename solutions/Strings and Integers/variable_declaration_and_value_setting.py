#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run variable-declaration-and-value-setting

# 1. In this very first mission you just need to help our bunch ofcyborgsto make friends! Look at the example in the editor, declare two variablesrobots, droidsand set their values to integers2, 5respectively. If you have any trouble, look at the hints below the description.
# 
# 2. When done, try to set values for variables from the previous paragraph in a single line likevar1, var2 = value1, value2(first variable gets first value etc.).
# 
# WhilePythonremains a dynamically typed language, meaning you don't have to specify types for variables, incorporating type annotations, especially in larger projects or when working in a team, can significantly enhance code quality and maintainability. It's worth noting that type annotations are optional, andPythonwill not enforce strict typing; they serve primarily as a development aid and documentation tool.
# 
# 3. For integers useinttype. Try to rewrite the task from the first paragraph with type annotations.
# 
# 
# END_DESC

a: int,  b: int = 2, 5
print(a)