from collections import deque

# las filas o rows tienen logica de COLAS
# osea FIFO (first in first out)
# como una cola en un supermercado


my_row = deque([1, 2])
# my_row.append(3)
# my_row.append(4)
# my_row.append(5)

print(my_row)

# en este caso tenemos 100 millones de elementos

# my_list = list(range(100_000_000))

my_row.popleft()
my_row.popleft()

print(my_row)


# esto evalua si el valor puede ser vacio o Falsy
# los valores Falsy pueden ser: "", 0, None y []
if not my_row:
    print("la fila esta vacia")
