str_text = input('Enter text: ')
str_text = str_text.replace(" ", "")
str_text = str_text.replace(",", "")
str_text = str_text.replace(":", "")
str_text = str_text.replace("!", "")
str_text = str_text.replace("?", "")
str_text = str_text.replace(";", "")
str_text = str_text.replace(".", "")
str_text = str_text.lower()
str_text2 = str_text[::-1]
if str_text == str_text2:
    print('It\'s palindrom')
else:
    print('It\'s not palindrom')