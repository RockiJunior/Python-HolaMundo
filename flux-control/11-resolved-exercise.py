"""resolved exercise"""

print("Bienvenidos a la calculadora")
print("Para salir escribe exit")
print("Las operaciones son suma, resta, multi, y div")


result = ""

while True:
    if not result:
        result = input("Ingrese un número: ")
        if result.lower() == "exit":
            break
        result = int(result)

    operation = input(
        "Por favor ingresa una operación ingresando uno de estos comandos: "
        "suma, resta, multi (multiplicación), div (división) : "
    )
    if operation.lower() == "exit":
        break

    n2 = input("Ingresa el siguiente número: ")
    if n2.lower() == "exit":
        break
    n2 = int(n2)

    if operation.lower() == "suma":
        result += n2
    elif operation.lower() == "resta":
        result -= n2
    elif operation.lower() == "multi":
        result *= n2
    elif operation.lower() == "div":
        result /= n2
    else:
        print("Operación no válida")
        continue

    print(f"El resultado de la operación es: {result}")
