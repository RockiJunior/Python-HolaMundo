numbers = [2, 4, 1, 45, 75, 22]

numbers.sort()  # esto lo ordena de menor a mayor

numbers.sort(reverse=True)  # esto lo ordena de mayor a menor

sorted_numbers = sorted(numbers)  # retorna una nueva instancia.

# users = [
#     [4, "Chanchito"],
#     [1, "Felipe"],
#     [5, "Pulga"],
# ]

# users.sort() # esto lo ordena de menor a mayor,
# print(users)

# pero que pasa si ponemos los ids al final?
# users = [
#     ["Chanchito", 4],
#     ["Felipe", 1],
#     ["Pulga", 5],
# ]
# print(users)

# siempre y cuando el primer elemento de la tupla sea algo ordenable (id)
# entonces lo va a ordenar de menor a mayor


# aunque le podemos indicar a sort
# con un lambda podemos hacer que lo ordene de la manera que queramos

users = [
    ["Chanchito", 4],
    ["Felipe", 1],
    ["Pulga", 5],
]


# def sortUsers(element):
#     return element[1]

# users.sort(key=sortUsers, reverse=True)

users.sort(key=lambda el: el[1], reverse=True)

print(users)