num = []

while True:
    n = int(input('Digite um valor: '))
    if n in num:
        print('Valor duplicado!!!, o valor não será adicionado')
    else:
        num.append(n)
        print('Valor adicionado com sucesso...')
    opc = ' '
    while opc not in 'SN':
        opc = input('Deseja continuar? [S/N] ').upper()
    if opc == 'N':
        break
print(sorted(num))