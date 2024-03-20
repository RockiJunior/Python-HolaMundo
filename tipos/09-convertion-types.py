
x = input("")

# int() -> convierte a integer
# str() -> convierte a string
# float() -> convierte a float
# bool() -> convierte a boolean

# el problema con el boolean es que este evalúa los datos que yo le coloque dentro
# y estos son evaluados y va a evaluarlos en true o false.
# para ello existe el concepto que se llama "Truthy" y "Falsy"

# en Falsy:
# - ""
# - 0 (numero cero)
# - none (objeto none)

# con esas 3 alternativas, bool() va a retornar False, en TODOS los casos contrarios, retornará True

print(x)