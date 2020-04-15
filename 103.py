def ficha(nome='<desconhecido>', gol=0):
    """
    -> Mostra uma string formatada com nome e quantidade de gols de um jogador.
    param nome: (Opcional) recebe o nome do jogador
    param gol : (Opcional) recebe a quantidade de gols do jogador
    """
    print(f'O jogador {nome} fez {gol} gol(s) no campeonato.')


# PROGRAMA PRINCIPAL

nome = input('Nome do jogador: ')
gol = input('Números de gols: ')
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if nome.strip() == '':
    ficha(gol=gol)
else:
    ficha(nome, gol)

