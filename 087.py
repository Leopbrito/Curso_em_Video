matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapares = 0
somaterc = 0
maiorsegundo = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            somapares += matriz[l][c]
        somaterc += matriz[l][2]
        if maiorsegundo ==0:
            maiorsegundo = matriz[1][c]
        if maiorsegundo < matriz[1][c]:
            maiorsegundo = matriz[1][c]
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^3}]', end=' ')
    print()
print(f'A soma do valores do pares {somapares}')
print(f'A soma da terceira coluna é {somaterc}')
print(f'O maior valor da segunda linha é {maiorsegundo}')