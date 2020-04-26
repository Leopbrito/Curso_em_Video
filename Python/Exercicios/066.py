num = {}
cont = -1
soma = 0
while True:
    cont += 1
    try:
        num[cont] = int(input('Digite números continuamente para somar todos(para parar digite 999): '))
        if num[cont] == 999:
            del(num[cont])
            break
    except ValueError:
        print('\033[31mERRO!!!, Só é permitida a entrada de números inteiro\033[m')
        num[cont] = int(input('Digite números continuamente para somar todos(para parar digite 999): '))
        if num[cont] == 999:
            del(num[cont])
            break
for x in num:
    soma += num[x]
print(f'Voce digitou {cont} números e soma deles é {soma}')
