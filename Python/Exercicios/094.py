grupo = list()
pessoa = dict()

while True:
    opc = ' '
    pessoa['nome'] = input('Nome: ').capitalize()
    pessoa['idade'] = int(input('Idade: '))
    pessoa['sexo'] = ' '
    while pessoa['sexo'] not in 'MF':
        pessoa['sexo'] = input('Sexo: [M/F] ').upper()
    grupo.append(pessoa.copy())
    pessoa.clear()
    while opc not in 'SN':
        opc = input('Deseja continuar: [S/N] ').upper()
    if opc == 'N':
        break

print(f'Ao todo, temos {len(grupo)} cadastradas')
somaidade = 0
for pessoa in grupo:
    for k, v in pessoa.items():
        if k == 'idade':
            somaidade += v
print(f'A média de idade do grupo é {somaidade/len(grupo):.0f}')
print('A mulheres cadastradas foram: ', end=' ')
for pessoa in grupo:
    if pessoa['sexo'] == 'F':
        print(pessoa['nome'], end=', ')
print('\nLista de pessoa com idade acima da média do grupo:')
for pessoa in grupo:
    if pessoa['idade'] > somaidade/len(grupo):
        print(f'Nome: {pessoa["nome"]:<10} | idade: {pessoa["idade"]:<3} | Sexo: {pessoa["sexo"]:<3}')
        