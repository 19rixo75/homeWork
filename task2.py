for x in range(0, 100):
    if x % 3 == 0 and x % 5 == 0:
        print(x, ' FizzBuzz')
    elif x % 3 == 0:
        print(x, ' Fizz')
    elif x % 5 == 0:
        print(x, ' Buzz')
    else:                   # Можно убрать, если не нужен весь список значений
        print(x)            #