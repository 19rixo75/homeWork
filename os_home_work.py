import os

file_list = os.listdir('needs_sorting')
os.makedirs('text_files', exist_ok=True)
os.makedirs('images', exist_ok=True)
for x in file_list:

    if x.split('.')[-1] == 'txt':
        from_file = os.path.join('needs_sorting', x)
        to_file = os.path.join('text_files', x)
        os.rename(from_file, to_file)
        with open('text_files/create_folder_text.txt', 'a', encoding='utf8') as write_file:
            write_file.write('\nName file: ' + x + '\nDate created file: ' + str(os.stat(to_file).st_ctime) + '\nSize file: ' + str(os.stat(to_file).st_size) + '\n')

    elif x.split('.')[-1] == 'jpg':
        from_file = os.path.join('needs_sorting', x)
        to_file = os.path.join('images', x)
        os.rename(from_file, to_file)
        with open('images/create_folder_images.txt', 'a', encoding='utf8') as write_file:
            write_file.write('\nName file: ' + x + '\nDate created file: ' + str(os.stat(to_file).st_ctime) + '\nSize file: ' + str(os.stat(to_file).st_size) + '\n')
