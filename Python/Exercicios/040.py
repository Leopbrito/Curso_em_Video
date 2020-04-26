n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2)/2
print('A média do aluno é {}'.format(media))
if media >= 7:
    print('O aluno está APROVADO!!!')
elif media >= 5 and media < 7:
    print('O aluno está de RECUPERAÇÂO!!!')
else :
    print('O aluno está REPROVADO!!!')