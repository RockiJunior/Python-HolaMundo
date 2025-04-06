# los diccionarios son una colección de datos
# que se encuentran agrupados por clave-valor
# son parecidos a los objetos tipo json


# como crear un diccionario

point = {
    "x": 25,
    "y": 50,
}

point["z"] = 100

# print(point["x"], point["y"])
# print(point)

if "lala" in point:
    print("i find lala", point["lala"])

# print(point.get("x"))
# print(point.get("lala")) # retorna None

# le podemos pasar un default para retornar si no encuentra el elemento
# print(point.get("lala", 97))


# como elimino una propiedad
# del point["y"]
# aunque también existe una función que se llama del y permite eliminar por propiedad
# del (point["x"])

# print(point)

# for value in point:
    # print(value) # imprime las claves
    # print(point[value]) # imprime los valores

# for value in point.items():
#     print(value)  # devuelve tuplas => ("x", 25), ("y", 50), ("z", 100)

for key, value in point.items():  # desestructurando
    print(key, value)  # devuelve las claves y los valores

users = [
    {"id": 1, "name": "Chanchito"},
    {"id": 2, "name": "Feliz"},
    {"id": 3, "name": "Gabriel"},
    {"id": 4, "name": "Felipe"},
]


for user in users:
    print(user["name"])
