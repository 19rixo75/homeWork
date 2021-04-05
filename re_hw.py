import re
# 1. Напишите регулярное выражение для поиска HTML-цвета, заданного как #ABCDEF, то есть # и содержит затем 3 или 6 шестнадцатеричных символов.
# 	HASH цвета используют значения от 0 до 15, где 0-9 цифры от нуля до 9, 10-15 буквы от A-F.

# rgb_search = '#13f, #152ABC, #FC12, #ffffff, #123654 '
# rgb_id = re.findall(r'(#[\da-fA-F]{3}[^\da-fA-F]|#[\da-fA-F]{6}[^\da-fA-F])', rgb_search)
# print(rgb_id)


# 2. Создать запрос для определения в тексте цифр, за которыми не стоит знак +.
# test_str = 'Примеры выражений “2*9-6*5” или (3+5)-9*4 '
# num_lst = re.findall(r'(\d)[^\+]', test_str)
# print(num_lst)


####  3 ###############################################################################

# time_str = '3. Найти в тексте время. Время имеет формат часы:минуты. И часы, и минуты состоят из двух цифр, пример: 09:00.' \
#            ' Напишите регулярное выражение для поиска времени в строке: «Завтрак в 9:00». Учтите, что «37:98» – некорректное время.' \
#            'Отображает 09:30 или 21:30. Кроме того, вы можете настроить способ времени в диалоговом окне "Формат ячеек".'
#
# matches = re.findall(r'[0-2][0-9]:[0-5][0-9]', time_str)
# print(matches)


# 4. Написать программу котороая будет выбирать из файла people.txt:
# 	1) Все имена и фамилии
# 	2) Все адреса
# with open('text_dir/people.txt', 'r', encoding='UTF8') as file:
#     people_data = file.read()
#
#     # Match all phones from file
#     pattern = re.compile(r'[A-Z][a-z]+ [A-Z][a-z][a-z][a-z]+')
#     matches = pattern.finditer(people_data)
#     i = 0
#     for match in matches:
#         i += 1
#         print(match)
#         print(i)


# #121 Hill St., Braavos‎ UT 92474
# with open('text_dir/people.txt', 'r', encoding='UTF8') as file:
#     people_data = file.read()
#
#     # Match all phones from file
#     pattern = re.compile(r'[0-9]+ [A-Z][a-z]+ [S][t]\., [A-Z][a-z]+ [A-Z][A-Z] [0-9]+')
#     matches = pattern.finditer(people_data)
#     i = 0
#     for match in matches:
#         i += 1
#         print(match)
#         print(i)



#
# 5. Написать регулярное выражение для проверки строки, задача определить состоит ли строка из символов a-z, A-Z, 0-

# data_str = 'dsaaaaaaaaaaaaa99999999999999999111'
# comp_data = re.compile("[a-zA-Z0-9*]+")
# vald = comp_data.match(data_str)
# if vald.group() == data_str:
#     print('Valid')
# else:
#     print('No valid')

#
# 6. Написать регулярное выражение для определения эстонского личного кода (isikukood)

# user_text_id = 'Проверка списка ID code 37510203725, 47503233714, 3880316, 4782, 375102037257'
# id_code = re.findall(r'([1-8][\d]{2}[0-1][\d][0-3][\d][0-7][\d]{3}[^\d])', user_text_id)
# print(id_code)
#
# Все строки произвольные.