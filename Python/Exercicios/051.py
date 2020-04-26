first = int(input('Primeiro termo da PA: '))
rz = int(input('Razão da PA: '))
tenth = first + 9 * rz
for x in range(first, tenth, rz):
    print('{} '.format(x), end='-> ')
print('FIM')