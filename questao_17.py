'''

Modifique o programa anterior de forma a ler um número n. Imprima os n primeiros números primos.

>> Questao anterior:
Escreva um programa que leia um número e verifique se é ou não um número primo. Para fazer essa
verificação, calcule o resto da divisão do número por 2 e depois por todos os números ímpares até o
número lido. Se o resto de uma dessas divisões for igual a zero, o número não é primo. Observe que 0 e 1
não são primos e que 2 é o único número primo que é par.

'''

aux = 1
div = 0

n = int(input("Informe um numero: "))

for i in range(n):
    for j in range(i+1):
        if (i+1) % (j+1) == 0:
            div = div + 1
    if div == 2:
        print(i+1)
    div = 0