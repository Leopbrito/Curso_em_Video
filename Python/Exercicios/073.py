times = ('Flamengo', 'Goiás', 'Palmeiras', 'Vasco', 'São Paulo', 'Santos', 'Grêmio', 'Athletico-PR', 'Corinthians', 'Fluminense', 'Bahia', 'CSA', 'Cruzeiro', 'Fortaleza', 'Internacional', 'Atlético-MG', 'Ceará', 'Botafogo', 'Avaí', 'Chapecoense')
print('-='*45)
print(f'Lista de Times do Brasileirão: {times}')
print('-='*45)
print(f'Os 5 primeiros: {times[:5]}')
print('-='*45)
print(f'Os 4 ultimos: {times[16:]}')
print('-='*45)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('-='*45)
print(f'O chapecoense está na {times.index("Chapecoense")+1}ª posição')
print('-='*45)