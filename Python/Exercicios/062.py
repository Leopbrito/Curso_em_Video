primeiro = int(input('Primeiro termo da PA: '))
rz = int(input('Razão da PA: '))
termo = primeiro
cont = 1
qtdtermo = 10
while cont <= qtdtermo:
    print(f'{termo}', end=" -> ")
    termo += rz
    if cont == qtdtermo:
        print('PAUSA')
        addtermo = int(input('Quantos termos voce quer mostrar a mais ?'))
        qtdtermo += addtermo 
    cont += 1
print(f'Progessão finalizada com {cont-1} termos mostrados')