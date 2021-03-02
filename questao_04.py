'''
questao_03:
fim = int(input("Digite o último número a imprimir:"))
x = 1
while x <= fim:
    print(x)
    x = x + 2

4) Reescreva o programa anterior para escrever os 10 primeiros múltiplos de 3.
'''


fim = 10
numero = 1
contador = 0

while contador < fim:

  if(numero % 3 == 0):
    print(numero)
    contador += 1

  numero += 1
  
  