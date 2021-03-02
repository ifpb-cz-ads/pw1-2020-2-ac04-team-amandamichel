'''2) Faça um programa para escrever a contagem regressiva do lançamento de um foguete. O programa deve imprimir 10, 9, 8, ..., 1, 0 e Fogo! na tela.'''
import time


quantidade = 10
numeros = list(range(1,quantidade+1))

while len(numeros) > 0:
  print(numeros.pop())
  time.sleep(1)

print('0... Fogo!')