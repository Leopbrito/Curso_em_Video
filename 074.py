from random import randint

num = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print(num)
print(f'O maior número é {max(num)}')
print(f'O menor número é {min(num)}')