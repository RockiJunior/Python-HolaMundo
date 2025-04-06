pets = [
    "Wolfgang",
    "Pelusa",
    "Pulga",
    "Felipe",
    "Pulga",
    "Chanchito feliz"
]


pets.insert(1, "Melvin")  # agrega al indice indicado

pets.append("Chanchito triste")  # agrega al final

# elimina la primera coincidencia, no el indice. solo funciona con un argumento y solo elimina el primero que encuentre
pets.remove("Pulga")

pets.pop(1)  # elimina el ultimo elemento, funciona con el indice

del pets[0]  # elimina el indice

pets.clear()  # elimina todo

print(pets)
