'''14) Escreva um programa para controlar uma pequena máquina registradora. Você deve solicitar ao usuário que digite o código do produto e a quantidade comprada. Utilize a tabela de códigos abaixo para obter o preço de cada produto.

Seu programa deve exibir o total das compras depois que o usuário digitar 0. Qualquer outro código deve gerar a mensagem de erro “Código inválido”.'''

cod_prod = int(input('Informe o código do produto ou 0 para encerrar: '))

precos = {
  1 : 0.5,
  2 : 1.0,
  3 : 4.0,
  5 : 7.0,
  9 : 8.0 }

total = 0

while cod_prod != 0:
  
  if (cod_prod in precos): 
    quantidade = int(input('\nInforme a quantidade: '))
    total += quantidade * precos[cod_prod]
  else:
    print('Código inválido\n')

  cod_prod = int(input('\nInforme o código do produto ou 0 para encerrar: '))

print(f'\nTotal das compras: R$ {total}')