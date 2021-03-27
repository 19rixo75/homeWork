def get_data_by_id(idcode):

    gender_num = idcode[0]
    by_num = idcode[1:3]
    bm_num = idcode[3:5]
    bd_num = idcode[5:7]
    region_num = idcode[7:10]
    chk_num = idcode[10]

    if int(gender_num) % 2 == 0:
        gend_id = 'Female'
    else:
        gend_id = 'Male'

    if gender_num == '1' or gender_num == '2':
        cent_id = '18'
    elif gender_num == '3' or gender_num == '4':
        cent_id = '19'
    elif gender_num == '5' or gender_num == '6':
        cent_id = '20'

    if 1 <= int(region_num) <= 10:
        region_id = 'Kuressaare haigla'
    elif 11 <= int(region_num) <= 19:
        region_id = 'Tartu Ülikooli Naistekliinik'
    elif 21 <= int(region_num) <= 150:
        region_id = 'Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn)'
    elif 161 <= int(region_num) <= 220:
        region_id = 'Rapla haigla, Loksa haigla, Hiiumaa haigla (Kärdla)'
    elif 221 <= int(region_num) <= 270:
        region_id = 'Ida-Viru keskhaigla (Kohtla-Järve, endine Jõhvi)'
    elif 271 <= int(region_num) <= 370:
        region_id = 'Maarjamõisa kliinikum (Tartu), Jõgeva haigla'
    elif 371 <= int(region_num) <= 420:
        region_id = 'Narva haigla'
    elif 421 <= int(region_num) <= 470:
        region_id = 'Pärnu haigla'
    elif 471 <= int(region_num) <= 490:
        region_id = 'Haapsalu haigla'
    elif 491 <= int(region_num) <= 520:
        region_id = 'Järvamaa haigla (Paide)'
    elif 521 <= int(region_num) <= 570:
        region_id = 'Rakvere haigla, Tapa haigla'
    elif 571 <= int(region_num) <= 600:
        region_id = 'Valga haigla'
    elif 601 <= int(region_num) <= 650:
        region_id = 'Viljandi haigla'
    elif 651 <= int(region_num) <= 700:
        region_id = 'Lõuna-Eesti haigla (Võru), Põlva haigla'

    print(gender_num, by_num, bm_num, bd_num, region_num, chk_num)
    print('You are ' + gend_id)
    print('You were born on ' + bd_num + '.' + bm_num + '.' + cent_id + by_num)
    print('Region code is ' + region_num + ' - ' + region_id)
    print('You check number is: ' + chk_num)
    user_menu()


def valid_id(idcode):


    # I astme kaal: 1 2 3 4 5 6 7 8 9 1
    summ_id_1 = 1 * int(idcode[0]) + 2 * int(idcode[1]) + 3 * int(idcode[2]) + 4 * int(idcode[3]) + \
                5 * int(idcode[4]) + 6 * int(idcode[5]) + 7 * int(idcode[6]) + 8 * int(idcode[7]) + \
                9 * int(idcode[8]) + 1 * int(idcode[9])
    rem_div_1 = summ_id_1 % 11
    val_1 = summ_id_1 - 11 * (summ_id_1 // 11)

    # II astme kaal: 3 4 5 6 7 8 9 1 2 3
    summ_id_2 = 3 * int(idcode[0]) + 4 * int(idcode[1]) + 5 * int(idcode[2]) + 6 * int(idcode[3]) + \
                7 * int(idcode[4]) + 8 * int(idcode[5]) + 9 * int(idcode[6]) + 1 * int(idcode[7]) + \
                2 * int(idcode[8]) + 3 * int(idcode[9])
    rem_div_2 = summ_id_2 % 11
    val_2 = summ_id_2 - 11 * (summ_id_2 // 11)

    # Test
    if rem_div_1 < 10 and rem_div_1 == int(idcode[10]) and val_1 == rem_div_1:
        print('The code was validated!')
    elif rem_div_2 == int(idcode[10]) and val_2 == rem_div_2 or rem_div_2 == 0:
        print('The code was validated!')
    else:
        print('The code did not pass validation!')

    user_menu()


def user_menu():
    print(user_id)
    user_choice = input('Please choose:\n1. Get data by ID code\n2. Check if ID is valid\n'
                        '3. Enter new ID for check\n4. Exit\n--> ')
    if user_choice == '1':
        get_data_by_id(user_id)

    elif user_choice == '2':
        valid_id(user_id)
    elif user_choice == '3':
        val_len_id()
        user_menu()
    elif user_choice == '4':
        quit()
    else:
        print('Choice out of range')
        user_menu()

def val_len_id():
    condition = True
    while condition:
        try:
            global user_id
            user_id = input('Please enter ID: ')
            int(user_id)
            if len(user_id) != 11:
                raise UserWarning
        except UserWarning:
            if len(user_id) < 11:
                print('Code is too short')
            elif len(user_id) > 11:
                print('Code is too long')
        except:
            print('Code you entered is not numeric')
        else:
            condition = False
            user_menu()

val_len_id()
