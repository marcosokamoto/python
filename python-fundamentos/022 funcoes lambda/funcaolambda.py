import os
os.system('cls')

def linha():
    print('-' * 50)

soma = lambda a , b: a + b
mult = lambda a, b, c:(a + b) * c
r = soma(2,5)
print(soma(2,5))
print(mult(2,5,3))
linha()

print((lambda a,b:a+b) (3,2))
linha()

r = lambda x, func: x + func(x)
res = r(2, lambda x:x*x)
print(res)
res=r(2, lambda x:x+3)
print(res)
