maiores = 0
homens = 0
mulheres = 0

while True:
    print('---'*10)
    print('Cadastrar Pessoa')
    print('---'*10)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo: [M/F] ').upper()
    print('---'*10)
    
    if idade > 17:
        maiores += 1
    if sexo == 'M':
        homens += 1
    if idade < 20 and sexo == 'F':
        mulheres += 1
    
    resp = ' '
    while resp not in "SN":
        resp = input('Quer continuar? [S/N] ').upper()
    if resp == 'N':
        break
print(f'''Total de pessoas maiores de idade: {maiores}
Quantidade de homens cadastrados: {homens}
Quantidade de mulheres com menos de 20 anos: {mulheres}
''')