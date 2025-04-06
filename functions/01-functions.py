def hola(name, lastname="Villarroel"): # el segundo argumento es considerado "opcional"
    print("Hola Mundo")
    print(f"Bienvenido {name} {lastname}")


hola(lastname="Gabriel", name="Villarroel") # argumentos nombrados
hola("Gabriel")
