#func
def numero_para_decimal(numero, base):
    decimal = int(numero, base)

    binario = bin(decimal)
    octal = oct(decimal)
    hexa = hex(decimal)

    print('Decimal : '+str(decimal))
    print('Binario : ' + str(binario[2:]))
    print('Octal : ' + str(octal[2:]))
    print('Hexadecimal : ' + str(hexa[2:].upper()))


#numero e base
numero = '1010'
base = 2

numero_para_decimal(numero, base)


l_binario['text'] = str(binario[2:])
        l_octal['text'] = str(octal[2:])
        l_decimal['text'] = str(decimal)
        l_hexadecimal['text'] = str(hexa[2:].upper())





