palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for p in palavras:
    print(f'Na palavra {p} temos ', end='')
    for l in p:
        if l in 'AEIOU':
            print(l, end=' ')
    print()