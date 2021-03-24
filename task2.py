for x in range(0, 100):
    if x % 3 == 0 and x % 5 == 0:
        print(x, ' FizzBuzz')
    elif x % 3 == 0:
        print(x, ' Fizz')
    elif x % 5 == 0:
        print(x, ' Buzz')
    else:                   # Можно убрать, если не нужен весь список значений
        print(x)            #


# Variant 2 (Вопрос: Почему функция выводит последнее значение None?)

# n = int(input('Введите верхнее значеие диапазона от 0 до '))
# def add(n):
#     for x in range(0, n):
#         if x % 3 == 0 and x % 5 == 0:
#             print(x, ' FizzBuzz')
#         elif x % 3 == 0:
#             print(x, ' Fizz')
#         elif x % 5 == 0:
#             print(x, ' Buzz')
#
# print(add(n))