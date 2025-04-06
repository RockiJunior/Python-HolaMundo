# from collections import deque

# las PILAS son una colección de datos
# que se encuentran agrupados por una estructura LIFO (last in first out)
# como una pila de libros
# osea el ultimo en entrar es el primero en salir


# my_stack = deque([1, 2, 3])
# my_stack.append(4)
# my_stack.append(5)
# my_stack.append(6)

# print(my_stack)

my_stack = []

my_stack.append(1)
my_stack.append(2)
my_stack.append(3)

print(my_stack)

# el metodo pop elimina el ultimo elemento y lo retorna
# osea que lo podemos guardar en una variable
last_item = my_stack.pop()

print(last_item)
print(my_stack)
print(my_stack[-1])  # imprime el ultimo elemento

last_item = my_stack.pop()
last_item = my_stack.pop()


if not my_stack:
    print("la pila esta vacia")
