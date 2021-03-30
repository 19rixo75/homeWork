#1 Написать программу, запрашивающую имя, фамилию и возраст пользователя и выводящую строку вида:
# Hello, <Фамилия пользователя> <Имя пользователя>. Your age is: <возраст>

# name, surname, age = input('Please enter your name, surname, and age. Use space separator: ').split()
# print('Hello, 'surname.capitalize() + ' ' + name.capitalize() + '. Your age is: ' + age + '.')

# 2 Напишите программу, которая находит длину гипотенузы для прямоугольного треугольника по двум катетам.
# (с = sqrt(a * a  +  b * b))

# a, b = input('Please enter said a and b. Use space separator: ').split()
# c = (int(a) ** 2  +  int(b) ** 2) ** 0.5
# print('Hypotenuse length: ' + str(c))

# 3 Пользователь вводит длины трех сторон треугольника (a,b,c) [тип float]. Напишите программу, которая проверяет,
# является ли треугольник прямоугольным (с2=a2+b2)

# a, b, c = input('Please enter sides A, B, and C. Use space separator: ').split()
# if float(c) ** 0.5 == float(a) ** 0.5 + float(b) ** 0.5:
#     print('This is a right triangle!')
# else:
#     print('It is not a right triangle!')

# 4 Пользователь вводит некоторый произвольный список list.
# Написать программу, выводящую элементы списка в обратном порядке.

# user_str = input('Please enter list. Use comma separator: ').split(',')
# user_str = user_str[::-1]
# print(list(user_str))

# 5 Как известно, кортеж является неизменяемым типом. Напишите программу, которая позволяет в кортеж A добавить кортеж B
# таким образом, что кортеж B помещается на index[2]. Пример: (1, 2, 3, 5, 8) (8,2,5) → (1, 2, 8, 2, 5, 3, 5, 8)

a = (1, 2, 3, 5, 8)
b = (8,2,5)
c = a[:2] + b + a[2:]
print(c)





