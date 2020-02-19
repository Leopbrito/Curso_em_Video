primeiro = int(input('Primeiro termo da PA: '))
rz = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo}', end=" -> ")
    termo += rz
    cont += 1
print('FIM')