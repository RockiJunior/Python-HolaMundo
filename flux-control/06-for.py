"""for"""

n1 = input(
    "Ingresa el numero a buscar dentro de un iterador de 5 elementos: ")
buscar = int(n1)

# range(5) es un iterable de python, y existen múltiples iterables dentro del lenguaje
# existen las listas y las tuplas. los strings también son iterables
for numero in range(5):
    if numero == buscar:
        print('encontrado', buscar)
        break
else:
    print("No se ha encontrado el numero:", buscar)

for char in "Ultimate Python":
    print(char)
