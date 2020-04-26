while True:
    n = int(input('Digite um número para ver sua tabuada: '))
    if n < 0 :
        break
    print('-=-'*6)
    for x in range(1,11):   
        print('{} x {:2} = {:2}'.format(n,x,n*x))
    print('-=-'*6)
