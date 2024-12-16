"""operadores_logicos"""

# and, or, not

gas = False
encendido = True
edad = 18

# el operador and tiene que tener ambos valores en true para pasar

# el operador or puede tener uno de dos, o más valores en true para pasar,
# pero si ambos son falsos entonces no va a pasar

# el operador not es para negar el valor true, o negar lo que se requiere preguntar

# if not gas and not encendido:
#     print("Puedes avanzar")


# if gas and (encendido or edad > 17):
#     print("Puedes avanzar")

# if not gas and (encendido or edad > 17):
#     print("Puedes avanzar")


# operador de corto circuito

# es cuando una operación es cancelada y sirve para ahorrar
# mucho tiempo de análisis de cómputo

# hay dos cases:

# utilizamos el operador and seguido de otro and:

# si solo el primer "and" da false, no va a continuar la ejecución del codigo,
# ejemplo
# if not gas and encendido and edad > 17:
# print("Puedes avanzar")

# utilizamos el operador or seguido de otro or:

# si solo el primer "or" da false, va a continuar la ejecución (contrario al "and")
# pero porque en el operador logico or, la primera instancia evalua por false.
# ejemplo:

# if not gas or encendido or edad > 17:
# print("Puedes avanzar")
