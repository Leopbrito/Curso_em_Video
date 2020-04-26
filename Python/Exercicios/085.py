lista = [[], []]
for x in range(1, 8):
    n = int(input(f'Digite o {x}º valor: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
print(f'Lista de pares: {sorted(lista[0])}')
print(f'Lista de impares: {sorted(lista[1])}')
