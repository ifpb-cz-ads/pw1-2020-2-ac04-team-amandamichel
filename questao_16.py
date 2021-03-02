'''16) Escreva um programa que leia um número e verifique se é ou não um número primo. Para fazer essa verificação, calcule o resto da divisão do número por 2 e depois por todos os números ímpares até o número lido. Se o resto de uma dessas divisões for igual a zero, o número não é primo. Observe que 0 e 1 não são primos e que 2 é o único número primo que é par.'''

numero = int(input('Informe um número: '))
divisor = 1
cont = 0

while (divisor <= numero):
  if (numero % divisor == 0):
    cont += 1
    divisor += 1
  else:
    divisor += 1

if (cont > 2):
  print(f'{numero} não é primo')
else:
  print(f'{numero} é primo')