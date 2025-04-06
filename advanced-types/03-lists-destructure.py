"""Desestructuración de listas"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# first, second, third = numbers
# print(first, second, third)

# esto es similar al spread operator en javascript solo que con asterisco

# first, *rest = numbers
# print(first, rest)

# first, second, *rest = numbers
# print(first, second, rest)

# first, *rest, third = numbers
# print(first, rest, third)

first, second, *rest, penu, last = numbers
print(second, penu)