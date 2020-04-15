grupo = []
pessoa = []

while True:
    opc = ' '
    nome = input('Nome: ').capitalize()
    peso = float(input('Peso: '))
    pessoa.append(nome)
    pessoa.append(peso)
    grupo.append(pessoa[:])
    pessoa.clear()
    while opc not in 'SN':
        opc = input('Deseja continuar: [S/N] ').upper()
    if opc == 'N':
        break

pesados = 0
leves = 0
for x in range(0, len(grupo)):
    if leves == 0:
        pesados = grupo[x][1]
        leves = grupo[x][1]
    if grupo[x][1] < leves:
        leves = grupo[x][1]
    if grupo[x][1] > pesados:
        pesados = grupo[x][1]
print('-=-'*30)
print(f'Ao todo, voce cadastrou {len(grupo)} pessoas.')
print(f'O maior peso foi {pesados}. Peso de', end=' ')
for x in grupo:
    if x[1] == pesados:
        print(x[0], end=', ')
print()
print(f'O menor peso foi {leves}. Peso de', end=' ')
for x in grupo:
    if x[1] == leves:
        print(x[0], end=', ')
