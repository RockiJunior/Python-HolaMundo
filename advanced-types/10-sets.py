# set significa grupo o conjunto
# y es una colección de datos que no se pueden repetir
# y que tampoco estan ordenados

first = {1, 1, 2, 2, 3, 4}
# first.add(5)
# first.remove(1)
# print(first)

second = [3, 4, 5]

second = set(second)
# => transforma una lista a set,
# pero tambien se puede hacer lo mismo con las tuplas

# este operador es para unir dos sets y quita los duplicados y se llama union
print(first | second)  # union

print(first & second)  # interseccion

print(first - second)  # diferencia

print(first ^ second)  # diferencia simétrica

# en los sets nosotros no podemos acceder a los elementos de manera directa como una lista

# second[0] # esto marcaria error

if 5 in second:
    print("exist")
