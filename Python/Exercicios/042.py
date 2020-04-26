print('-+'*20)
print('Analisador de triangulo')
print('-+'*20)
r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a primeira reta: '))
r3 = float(input('Digite a primeira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É possivel fazer um triangulo')
    if r1 == r2 == r3:
        print('Equilatero')
    elif r1 != r2 != r3 != r1:
        print('Escaleno')
    else:
        print('Isósceles')
else:
    print('Não é possivel fazer um triangulo')