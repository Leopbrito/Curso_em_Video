from datetime import date

nasc = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - nasc
diff = abs(idade - 18)

print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade > 18:
    print('Voce deveria ter se alistado em {}, há {} ano(s) atrás'.format((atual-diff), diff))
elif idade < 18:
    print('Voce deverá se alistar em {}, daqui à {} ano(s)'.format((atual+diff), diff))
else :
    print('Voce deverá se alistar esse ano.')