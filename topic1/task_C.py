# C. Телефонные номера

def clean_phone(phone):
    phone = list(phone)
    phone_clean = []
    for symb in phone:
        if symb.isdigit():
            phone_clean.append(symb)
    lpc = len(phone_clean)
    if lpc == 7:
        code = ['4', '9', '5']
        tel = phone_clean
    elif lpc == 11:
        code = phone_clean[1:4]
        tel = phone_clean[4:]
    else:
        print('error')
    return code+tel

phone_to_check = clean_phone(input())


for _ in range(3):
    phone_from_book = clean_phone(input())
    is_equal = True
    for i in range(10):
        if phone_from_book[i] != phone_to_check[i]:
            is_equal = False
            break
    print('YES' if is_equal else 'NO')
