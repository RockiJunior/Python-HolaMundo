"""EJERCICIOS DE PYTHON CON TIPOS AVANZADOS"""

# 1. Eliminar los espacios en blanco de un string
# y devolver una lista con los caracteres restantes

str_1 = "  hola  mundo  "

# rest_characters = list(str_1.replace(" ", ""))
# print(rest_characters)


def remove_spaces(string):
    return [char for char in string if char != " "]


print(remove_spaces(str_1))

# 2. Contar en un diccionario cuanto se repiten
# los caracteres de un string (como una funcion que devuelve un diccionario)
# pero recibe un string

exer_2 = {
    "a": 2,
    "b": 1,
    "c": 1
}

# 3. Ordenar las llaves de un diccionario
# por el valor que tienen y devolver una lista
# que contiene tuplas [("a", 3), ("b", 2), ("c", 4), ("d", 4)]

# 4. De un listado de tuplas [("a", 1), ("b", 2), ("c", 4), ("d", 3)]
# devolver la tuplas que contengan el mayor valor

# 5. Crear un mensaje que diga:
# "Los caracteres que más se repiten con 4 repeticiones son: "
# Formar una lista con los caracteres que mas se hayan repetido.
# los caracteres devueltos tienen que estar en mayuscula
#

# 6. Juntar la solución de los ejercicios anteriores
# para encontrar los caracteres que más se repiten
# de un string
