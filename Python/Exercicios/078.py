num = []

for x in range(0,5):
    n = int(input(f'Digite o valor para a posição {x}: '))
    num.append(n)
print(f'Os valores digitados foram {num}')
print(f'O maior valor digitado foi {max(num)} nas posições', end=' ')
for i, v in enumerate(num):
    if v == max(num):
        print(i, end='... ')
print()
print(f'O maior valor digitado foi {min(num)} nas posições', end=' ')
for i, v in enumerate(num):
    if v == min(num):
        print(i, end='... ')