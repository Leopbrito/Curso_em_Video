n = int(input('Digite um número para ver sua tabuada: '))
for x in range(1,11):
    print('{} x {:2} = {:2}'.format(n,x,n*x))