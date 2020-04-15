def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número.
    param n : O numero a ser calculado
    param show : (Opcional), mostrar ou nao a conta.
    return: nao retorna
    """
    fat = n
    if show == True:
        print(n, end=' ')
    while n != 1:
        if show == True:
            print(f'x {n-1:.0f}', end=' ')
        n -= 1
        fat = fat * n
    if show == True:
        print(f'= {fat}')
    else:
        print(fat)


fatorial(5, True)
print(help(fatorial))

