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

# a = (1, 2, 3, 5, 8)
# b = (8,2,5)
# c = a[:2] + b + a[2:]
# print(c)

# 6 *Написать программу, которая для произвольного списка находит число / числа, наиболее часто встречающееся в
# данном списке и возвращающее их также в виде списка.
#         Примеры:
#         [1, 2, 3, 4, 7, 9, 9] → [9]
#         [1, 2, 4, 6, 4, 6] → [4,6]

# a = [1, 2, 3, 4, 7, 9, 9]
# c = {i:a.count(i) for i in a}
# print(c)
# print(max(c, key = c.get))

# 7 *Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.
#
#         Примеры:
#         1234565 seconds = 14:6:56:5


# user_sec = int(input('Введите количество секунд: '))
# sec_id = user_sec % 60
# min_id = user_sec // 60 % 60
# hour_id = user_sec // 3600 % 24
# day_id = user_sec // 3600 // 24
# print(str(day_id) + ':' + str(hour_id) + ':' + str(min_id) + ':' + str(sec_id))









