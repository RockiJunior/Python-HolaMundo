users = [
    ["Chanchito", 4],
    ["Felipe", 1],
    ["Pulga", 5],
]

# transformación:

# names = []
# for user in users:
#     names.append(user[0])

# print(names)

# una manera mas elegante de escribir lo mismo...
# names = [user[0] for user in users]

# filtración:

# se coloca user for user in user...porque con el primer argumento
# indico que quiero retornar el elemento completo, y no como el
# user[0] caso anterior

# filtrar si el segundo argumento (id) es mayor a 2
# names = [user for user in users if user[1] > 2]


# filtración y transformación:
# names = [user[0] for user in users if user[1] > 2]

users = [
    ["Chanchito", 4],
    ["Felipe", 1],
    ["Pulga", 5],
]
# transformar con lambda y map
# names = list(map(lambda user: user[0], users))

# filtrar con lambda y filter
# names = list(filter(lambda user: user[1] > 2, users))

# filtrar y transformar con filter, map y lambda
names = list(map(lambda user: user[0], filter(lambda user: user[1] > 2, users)))

print(names)
