pets = ["Pelusa", "Pulga", "Felipe", "Chanchito feliz"]

# for pet in pets:
#     print(pet)  # esto devuelve simplemente los elementos

# el enumerate genera una tupla. sirve mucho para acceder al indice que necesitamos iterar
# for pet in enumerate(pets):
#     # print(pet) # esto devuelve una tupla con el indice y el valor => "(0, "Pelusa")""
#     print(pet[0]) # devuelve el indice
#     print(pet[1]) # devuelve el valor


# se pueden desestrucutar las tuplas para obtener el indice y el valor
for index, pet in enumerate(pets):
    print(index, pet)