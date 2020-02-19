from math import radians, cos, sin, tan

an = float(input('Digite um ângulo: '))
sen = sin(radians(an))
cos = cos(radians(an))
tan = tan(radians(an))
print('O ângulo de {:.0f}º tem o SENO de {:.2f}, o COSSENO de {:.2f} e a TANGENTE de {:.2f}'.format(an,sen,cos,tan))