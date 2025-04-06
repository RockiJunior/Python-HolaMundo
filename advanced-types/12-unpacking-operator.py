my_list = [1, 2, 3, 4]

# print(1, 2, 3, 4)  # si yo quisiera imprimir los elementos de my_list

# print(*my_list)

my_list_2 = [5, 6]

combined_list = ["Hola", *my_list, "Mundo", *my_list_2, "Chanchito"]

print(combined_list)


# este operador tambien se puede utilizar en los diccionarios


point = {
    "x": 19,
    "y": 15
}

point_2 = {
    "z": 10,
    "w": 20
}

# si yo tengo una propiedad que se llama igual en ambos diccionarios, se va a pisar
# el valor del primero con el valor del segundo

combined_point = {**point, **point_2}

print(combined_point)
