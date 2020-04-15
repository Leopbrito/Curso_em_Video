num = []

while True:
    n = int(input('Digite um valor: '))
    num.append(n)
    opc = ' '
    while opc not in 'SN':
        opc = input('Deseja continuar? [S/N] ').upper()
    if opc == 'N':
        break
print(f'A lista contem {len(num)} elementos.')
print(f'A lista na ordem decrescente: {sorted(num, reverse=True)}')
if 5 in num:
    print('O valor 5 \033[32mFOI\033[m encontrado na lista.')
else:
    print('O valor 5 \033[31mNÃO FOI\033[m encontrado na lista.')