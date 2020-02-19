qtd = int(input('Quantos termos voce quer mostrar? '))
fibonacci = 0
nant = 1
while qtd != 0:
    print(f'{fibonacci}', end=" -> ")
    fibonacci += nant
    nant = fibonacci - nant
    qtd -= 1
print('FIM')