def escreva(txt):
    x = len(txt)+10
    print('~'*x)
    print(f'{txt:^{x}}')
    print('~'*x)

escreva('Leo')

escreva('Curso em video')