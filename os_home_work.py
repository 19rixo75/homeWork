import os

file_list = os.listdir('../homeWork/needs_sorting')
os.makedirs('../homeWork/text_files', exist_ok=True)
os.makedirs('../homeWork/images', exist_ok=True)
for x in file_list:

    if x.split('.')[-1] == 'txt':
        from_file = os.path.join('../homeWork/needs_sorting', x)
        to_file = os.path.join('../homeWork/text_files', x)
        os.rename(from_file, to_file)
        with open('../homeWork/text_files/create_folder_text.txt', 'a', encoding='utf8') as write_file:
            write_file.write('\nName file: ' + x + '\nDate created file: ' + str(os.stat(to_file).st_ctime) + '\nSize file: ' + str(os.stat(to_file).st_size) + '\n')

    elif x.split('.')[-1] == 'jpg':
        from_file = os.path.join('../homeWork/needs_sorting', x)
        to_file = os.path.join('../homeWork/images', x)
        os.rename(from_file, to_file)
        with open('../homeWork/images/create_folder_images.txt', 'a', encoding='utf8') as write_file:
            write_file.write('\nName file: ' + x + '\nDate created file: ' + str(os.stat(to_file).st_ctime) + '\nSize file: ' + str(os.stat(to_file).st_size) + '\n')