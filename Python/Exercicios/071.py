print('---'*10)
print('Banco Leopbrito ')
print('---'*10)
valor = int(input('Digite o valor a sacar: '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'O total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('---'*10)
print('Volte sempre!!!')
print('---'*10)