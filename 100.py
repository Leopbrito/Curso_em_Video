from random import randint
from time import sleep

numeros = list()

def sorteia():
    print('Sorteando 5 valores:', end=' ')
    for x in range(0,5):
        n = randint(0,10)
        numeros.append(n)
        print(n, end=' ', flush=True)
        sleep(0.5)
    print('Pronto!')


def somaPar():
    soma = 0
    for x in numeros:
        if x % 2 == 0:
            soma += x 
    print(f'somando os valores pares de {numeros}, temos {soma}')

sorteia()
somaPar()