#import da biblioteca
from sympy import fibonacci


#definição da sequência de fibonacci
def sequencia_fibonacci(i):
    if i < 0:
        return False
    
    n = 0
    while True:
        fib_n = fibonacci(n)
        if fib_n == i:
            return True
        elif fib_n > i:
            return False
        n += 1


#main
numero = int(input("Digite o valor desejado: "))

if sequencia_fibonacci(numero):
    print(f'o valor {numero} pertence a sequência de fibonacci')
else:
    print(f'o valor não pertence a sequência de fibonacci')


