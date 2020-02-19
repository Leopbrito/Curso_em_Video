num = int(input('Digite um número inteiro:'))
print('''Escolha a base de conversão
[1] CONVERSÃO PARA BINÁRIO
[2] CONVERSÃO PARA OCTAL
[3] CONVERSÃO PARA HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é {}'.format(num, bin(num)))
elif opção == 2:
    print('{} convertido para OCTAL é {}'.format(num, oct(num)))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é {}'.format(num, hex(num)))