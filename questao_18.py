'''18) Escreva um programa que calcule o resto da divisão inteira entre dois números. Utilize apenas as operações de soma e subtração para calcular o resultado.'''

dividendo = int(input('Informe o dividendo: '))
divisor = int(input('Informe o divisor: '))
contador = 0

while dividendo >= divisor:
  resto = dividendo - divisor
  dividendo -= divisor
  contador += 1

print(f'\nResto: {resto}')