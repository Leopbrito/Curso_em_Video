def calc_area(l, c):
    a = l * c
    return a

#PROGRAMA PRINCIPAL
print(f'{"Controle de Terrenos":^30}')
print('-'*30)
l = float(input('Digite a largura(m): '))
c = float(input('Digite a comprimento(m): '))
a = calc_area(l, c)
print(f'A area de um terreno {l}x{c} é {a}m²')