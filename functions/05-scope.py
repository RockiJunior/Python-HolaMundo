# segun la comunidad de python las variables globales son mala practica
greeting = "Hello Global"


# def greet():
#     global greeting
#     print(greeting)


def greet():
    greeting = "Hello World"
    print(greeting)


def greetPig():
    greeting = "Hello Pig"
    print(greeting)


greet()
print(greeting)
