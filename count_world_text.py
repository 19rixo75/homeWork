# Домашнее задание:
# Написать программу, которая открывает заданый пользователем файл, считает количество слов, и количество уникальных
# слов (если это слово уже посчитанно, то второй раз не считает)
# Примеры:
# Программа = программа
# Программа, = программа
# Рыбачить и рыбачит это разные слова
# Т.е. Знаки препинания в конце слова и регистр букв не должны влиять на уникальность
# Результат записать в текстовый файл : название файла, количество слов, количество уникальных слов
unic_word = input('Please enter word for search: \n--> ')
with open('text_dir/text_1.txt', 'r', encoding='utf8') as read_file:
    file_content = read_file.read()
    file_content = file_content.replace(",", "").replace(":", "").replace("!", "").replace("?", "").replace(";", "").replace(".", "")
    word_content = len(file_content)
    count_word = file_content.count(unic_word)
    list_pr_tx = [read_file.name, word_content, count_word]
    header = ['Name_file', 'Unic_name', 'Count', 'Words']
    with open('text_dir/info_text.txt', 'a', encoding='utf8') as write_file:
        write_file.write(header[0] + '               ' + header[1] + '  ' + header[2] + '  ' + header[3] + '\n')
        write_file.write(str(list_pr_tx[0]) + '     ' + unic_word + '         ' + str(list_pr_tx[2]) + '     ' + str(list_pr_tx[1]) + '\n')
