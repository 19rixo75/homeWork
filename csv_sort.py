import csv

user_choice = int(input('Please choose by sorted:\n1. Country or region\n2. Score\n3. GDP per capita\n4. Social support\n'
                    '5. Healthy life expectancy\n6. Freedom to make life choices\n7. Generosity\n'
                    '8. Perceptions of corruption\n--> '))

top_num = int(input('Please enter top: '))

with open('csv_files/2019.csv', 'r', encoding='UTF8') as csv_file:
    csv_reader = csv.reader(csv_file)
    if user_choice == 1:
        csv_reader = sorted(csv_reader, key=lambda x: x[user_choice])
    else:
        csv_reader = sorted(csv_reader, key=lambda x: x[user_choice], reverse=True)
    for line in csv_reader[:(top_num + 1)]:
        print(line)