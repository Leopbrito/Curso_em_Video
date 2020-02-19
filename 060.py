num = float(input('Digite um número para calcular seu fatorial: '))
fat = num 
print(f'{num:.0f}! = {num:.0f}', end=' ')
while num != 1:
    num -= 1
    print(f'x {num:.0f}', end=' ')
    fat = fat * num 
print(f'= {fat:.0f}')