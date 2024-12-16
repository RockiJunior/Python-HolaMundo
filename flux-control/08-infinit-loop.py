"""infinit-loop"""

# es tremendamente importante evitar los loops infinitos para evitar
# consumir la memoria del servidor o pc.
# para ello lo mas importante dentro de un loop infinito (pocos utilizados pero útiles)
# es la instrucción de break

comand = ""

while True:
    comando = input("$ ")
    print(comando)
    if comando.lower() == "exit":
        break  # sin esta instrucción el loop va a consumir la memoria del pc o servidor
