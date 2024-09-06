print('Enter a demical number: ')
decNum = input()

print('Choose the conversion you want to perform first: ')
print('1. Decimal to Binary')
print('2. Decimal to Octal')
print('3. Decimal to Hexadeximal')
print('Enter your choice (1/2/3)')
choice = input()

if choice == '1':
    print('Decimal to Binary Conversion')
    binarynumber = bin(int(decNum))
    print('The Binary representation of ' ,decNum, 'is ' ,binarynumber)
elif choice == '2':
    print('Decimal to Octal Conversion')
    octalnumber = oct(int(decNum))
    print('The Octal representation of ', decNum, 'is ', octalnumber)

elif choice == '3':
    print('Decimal to Hexadecimal Conversion')
    hexadecimalnumber = hex(int(decNum))
    print('The HexaDecimal representation of ', decNum, 'is ', hexadecimalnumber)
else:
    print('Invalid input!!!')
