while True :
    chooseChoice = input(f'Put your base number type ???\n1. Binary\n2. Decimal\n3. Hexadecimal\n4. Exit \n: ')
    if chooseChoice == '1':
        # 2 -> all
        binary_number2 = input(f'Put your number : ')
        decimal_number2 = int(binary_number2, 2)
        hexadecimal_number2 = hex(decimal_number2)[2:]
        print('====================')
        print("decimal:", decimal_number2)
        print("Hexadecimal:", hexadecimal_number2.upper())
        print('====================')
    elif chooseChoice == '2':
        # 10 -> all
        decimal_number10 = int(input(f'Put your number : '))
        binary_number10 = bin(decimal_number10)[2:]
        hexadecimal_number10 = hex(decimal_number10)[2:]
        print('====================')
        print("binary:", binary_number10)
        print("Hexadecimal:", hexadecimal_number10.upper())
        print('====================')
    elif chooseChoice == '3':
        # 16 -> all
        hexadecimal_number16 = input(f'Put your number : ')
        decimal_number16 = int(hexadecimal_number16, 16)
        binary_number16 = bin(decimal_number16)[2:] 
        print('====================')
        print("binary:", binary_number16)
        print("decimal:", decimal_number16)
        print('====================')
    elif chooseChoice == '4':
        print('====================')
        print('Exit.')
        print('====================')
        break
    else:
        print('====================\n please try again.\n====================')
        continue