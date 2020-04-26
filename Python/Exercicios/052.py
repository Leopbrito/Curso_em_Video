n = int(input('Digite um número: '))
tot = 0
for x in range(1, n+1):
    if n % x == 0:
        print('\033[33m{}\033[m'.format(x), end=' ')
        tot += 1
    else:
        print('\033[31m{}\033[m'.format(x), end=' ')
if tot ==2:
    print('\n{} É um número PRIMO'.format(n))
else:
    print('\n{} NÃO é um númeor PRIMO'.format(n))