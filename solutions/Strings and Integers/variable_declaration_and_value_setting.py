#!/usr/bin/env checkio --domain=py run variable-declaration-and-value-setting

# 1. In this very first mission you just need to declare two variablesa, band set their values to integers2, 5respectively.
# 
# 2. When done, try to set values for variables in a single line (first variables gets first value etc.).
# 
# WhilePythonremains a dynamically typed language, meaning you don't have to specify types for variables, incorporating type annotations, especially in larger projects or when working in a team, can significantly enhance code quality and maintainability. It's worth noting that type annotations are optional, andPythonwill not enforce strict typing; they serve primarily as a development aid and documentation tool.
# 
# 3. For integers useinttype. Rewrite the first variant with type annotation.
# 
# 
# END_DESC

a: int,  b: int = 2, 5
print(a)