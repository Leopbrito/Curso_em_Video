from time import sleep

def contador(i, f, p):
    print(f'contagem de {i} à {f} de {p} em {p}')
    c = i
    if i < f:
        while c <= f:
           print(c, end=' ', flush=True)
           c += p
           sleep(0.5)
        print('FIM')
    else:
        while c >= f:
            print(c, end=' ', flush=True)
            c -= p
            sleep(0.5)
        print('FIM')

contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!!!')
i = int(input('inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)