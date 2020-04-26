num = {}
cont = -1
soma = 0
while True:
    cont += 1
    num[cont] = input('Digite números continuamente para somar todos(para parar digite "S"): ')
    if num[cont].isnumeric() == True:
        num[cont] = int(num[cont])
    if num[cont] == 'S' or num[cont] == 's':
        del(num[cont])
        break
    if str(num[cont]).isnumeric() == False:
        del(num[cont])
        print('Só é permitida a entrada de números')
        cont -= 1 
for x in num:
    soma += num[x]
print(f'Voce digitou {cont} números e soma deles é {soma}')
