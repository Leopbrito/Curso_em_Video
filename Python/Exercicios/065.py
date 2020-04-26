maior = 0
menor = 0
cont = ''
while cont != 'N':
    num = float(input(f'Digite um número: '))
    if menor == 0 and maior == 0:
        maior = num
        menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    cont = input('Voce quer continuar [S/N]').upper()
print(f'O maior valor é {maior} e o menor valor é {menor}')
