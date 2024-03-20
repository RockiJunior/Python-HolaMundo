n1 = input("Ingresa el primer numero: ")
n2 = input("Ingresa el segundo numero: ")

n1 = int(n1)
n2 = int(n2)

suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = n1 / n2


mensaje = f"""de la suma esde la suma es
    Para los números {n1} y {n2},
    el resultado de la suma es {suma}.de la suma es
    el resultado de la resta es {resta}.de la suma es
    el resultado de la multiplicación es {multi}.
    el resultado de la división es {div}.
"""
print(mensaje)
