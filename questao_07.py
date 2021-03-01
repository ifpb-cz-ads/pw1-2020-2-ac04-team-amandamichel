'''

Escreva um programa que leia dois números. Imprima o resultado da multiplicação do primeiro pelo segundo.
Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos
entender a multiplicação de dois números como somas sucessivas de um deles. Assim,
4 × 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.

'''

n1 = int(input("Informe um valor: "))
n2 = int(input("Informe outro valor: "))

resultado = 0

for i in range(n2):
    if i == n2-1:
        print(n1)
    else:
        print(n1, "+", end=" ")
    resultado = resultado + n1
print("O resultado de ", n1 , " X ", n2, " = ", resultado)