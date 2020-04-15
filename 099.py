from random import randint
numeros = list()

def maior(n):
    numeros.clear()
    print('-'*60)
    print('Analisando numeros passados...')
    for x in range(0,n):
        numeros.append(randint(0,10))
        print(numeros[x], end=' ')
    print(f'foram informados {len(numeros)} valores ao todo')
    mai = 0
    for x in numeros:
        if mai == 0:
            mai = x
        if x > mai:
            mai = x
    print(f'O maior valor informado foi {mai}')
    print('-'*60)

maior(6)
maior(3)
maior(0)