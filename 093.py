jogador = dict()

def linha():
    print('-='*30)

jogador['nome'] = input('Nome: ')
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
jogador['gols'] = gols = list()
for x in range(1, partidas+1):
    g = int(input(f'Quantos gol na partida {x}? '))
    gols.append(g)
jogador['total'] = sum(gols)
linha()
print(jogador)
linha()
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
linha()
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for x in range(1, partidas+1):
    print(f'=> na partida {x}, fez {gols[x-1]}')
print(f'foi um total de {jogador["total"]} gols')
