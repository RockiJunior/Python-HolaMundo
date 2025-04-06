def suma(*numbers):
    result = 0
    for number in numbers:
        result += number
    print(result)


suma(2, 5, 10, 2, 4)
