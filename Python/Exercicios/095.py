time = list()
jogador = dict()
iden = 0

def linha():
    print('-='*30)

while True:
    jogador['cod'] = iden
    jogador['nome'] = input('Nome: ')
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    jogador['gols'] = gols = list()
    for x in range(1, partidas+1):
        g = int(input(f'Quantos gol na partida {x}? '))
        gols.append(g)
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    jogador.clear()
    iden += 1
    opc = ' '
    while opc not in "SN":
        opc = input('Deseja continuar [S/N]? ').upper()
    if opc == 'N':
        break
linha()
print(f'{"cod":<3} | {"Nome":<10} | {"GOLS":<20} | {"Total":<5}')
for jogador in time:
    print(f'{jogador["cod"]:<3} | {jogador["nome"]:<10} | {str(jogador["gols"]):<20} | {jogador["total"]:<5}')
linha()
while True:
    opc = int(input('Mostrar dados de qual jogador? [999 para sair]'))
    if opc == 999:
        break
    else:
        for jogador in time:
            if jogador['cod'] == opc:
                print(f'Levantamento do jogador: {jogador["nome"]}')
                for x in range(1, len(jogador['gols'])+1):
                    print(f'=> na partida {x}, fez {jogador["gols"][x-1]}')
                print(f'foi um total de {jogador["total"]} gols')
                linha()
