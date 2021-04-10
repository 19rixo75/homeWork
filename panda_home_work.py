import pandas as pd

df = pd.read_csv('csv_files/survey_results_public.csv')
df = df[['Respondent',  'Hobbyist', 'Age', 'Country',  'CurrencyDesc', 'CurrencySymbol']]

def user_menu():
    user_choice = input('Please choose:\n1. Средний возраст пользователей\n2. Группирует по хобби/профессионал\n'
                        '3. Группирует по стране проживания\n4. Группирует по валюте зарплаты\n5. Выход\n--> ')
    if user_choice == '1':
        print(df.mean()[1])
        user_menu()
    elif user_choice == '2':
        print(df['Hobbyist'].value_counts())
        user_menu()
    elif user_choice == '3':
        print(df.groupby('Country').mean())
        user_menu()
    elif user_choice == '4':
        print(df.groupby('CurrencyDesc').mean())
        user_menu()
    elif user_choice == '5':
        quit()
    else:
        print('Choice out of range')
        user_menu()

user_menu()