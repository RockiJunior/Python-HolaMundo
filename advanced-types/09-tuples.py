# tupleNumbers = (1, 2, 3)
# esto es lo mismo que hacer una concatenación
tupleNumbers = (1, 2, 3) + (4, 5, 6)

# print(tupleNumbers)

# quiero transformar a tupla
# point = tuple([1, 2])

# print(point)

# lessNumbers = tupleNumbers[:2]

# print(lessNumbers)

# first, second, *others = tupleNumbers

# print(first, second, others)

# for item in tupleNumbers: 
#     print(item)

numbersList = list(tupleNumbers)

numbersList[0] = "Chanchito Feliz"

print(numbersList)