"""my exercise"""

# verificar si es que ya hemos ingresado un número antes
# en el caso de que no haya sido ingresado un número, le debemos ingresar
# al usuario que tenemos que ingresar un número.


# si el usuario ya ha ingresado un número antes
# debemos pedirle al usuario que ingrese una operación
# en el caso de que hayamos solicitado un número,
# le vamos a indicar que tiene que ingresar la operación


# luego de ingresar la operación, le vamos a pedir al usuario
# que ingrese otro número y despues de esto nosotros vamos a mostrar
# los resultados

# una vez que hayamos mostrado el resultado, nosotros lo vamos a guardar como el primero numero+
# como si fuese una especie de bucle.

# mi codigo: 

command = ""
operation = ""
result = None

while command.lower() != "exit":
    if result is None:
        print("Hola! Bienvenido a la calculadora!!! Veo que aún no has ingresado ningún valor...")

    n1 = input(
        "Por favor intenta ingresar un valor, para poder realizar una operación: "
    )

    n1 = int(n1)

    operation = input(
        "Por favor ingresa una operación ingresando uno de estos comandos: "
        "sum (suma), rest (resta), product (multiplicacion), divition (división): "
    )

    n2 = input("Por favor ingresa el segundo valor: ")
    n2 = int(n2)

    if operation == "sum":
        result = n1 + n2
    if operation == "rest":
        result = n1 - n2
    if operation == "product":
        result = n1 * n2
    if operation == "divition":
        result = n1 / n2

    print("El resultado de la operación es:", result)
