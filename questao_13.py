'''

Escreva um programa que leia números inteiros do teclado. O programa deve ler os números até que o usuário
digite 0 (zero). No final da execução, exiba a quantidade de números digitados, assim como a soma e a média
aritmética.

'''

soma = 0
quantidade = 0

while True:
    num = int(input("Informe um valor: "))
    if num == 0:
        break;
    else:
        quantidade = quantidade + 1
        soma = soma + num
print("\nSoma: ", soma)
print("Quantidade de numeros digitados: ", quantidade)
print("Media: ", soma/quantidade)