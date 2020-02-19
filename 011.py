larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = alt * larg
print('A medidas da parede é {:.2f}x{:.2f} e a área é {:.2f}m²'.format(larg,alt,area))
tinta = area / 2
print("A quantidade de tinta necessaria é {:.2f}l".format(tinta))