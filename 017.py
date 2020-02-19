from math import hypot

'''
metodo sem importação

co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('O comprimento do hipotenusa é {:.2f}'.format(hi))
'''

co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('O comprimento da hipotenusa é {:.2f}'.format(hi))
