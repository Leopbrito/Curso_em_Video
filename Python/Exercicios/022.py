nome = input('Digite seu nome completo: ').strip()
print('Seu nome tem ao todo {} caracteres'.format(len(nome)))
print('Seu nome em maiusculo: {}'.format(nome.upper()))
print('Seu nome em minusculo: {}'.format(nome.lower()))
print('Seu nome capitalizado: {}'.format(nome.title()))
separa = nome.split()
print('Seu primeiro nome é {} e tem ao todo {} caracteres'.format(separa[0],len(separa[0])))
