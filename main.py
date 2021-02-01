def mask_security_number(security_number):
    list_security_number = []
    a = 0
    b = 1
    while a < len(security_number):
        list_security_number.append(security_number[a])
        a += 1
    while b < 5:
        list_security_number[len(security_number) - b] = "*"
        b += 1
    return ''.join(list_security_number)

print(f'example number : {mask_security_number("901212-1221123")}')
registration_number = input(f'Please input your registration number : ')
if len(registration_number) == 14 or len(registration_number) == 13:
    print(f'Secured your registaration number is {mask_security_number(registration_number)}')
else:
    print("You input wrong number!")