'''12) Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal. Pergunte também o valor mensal que será pago. Imprima o número de meses para que a dívida seja paga, o total pago e o total de juros pago.'''

divida = float(input('Informe o valor da dívida: '))
taxa_juros = float(input('Informe a taxa de juros mensal: '))/100
pgmt_mensal = float(input('Informe quando será pago por mês: '))

meses = 0
total_juros = 0
total_pago = 0
meses = 0

while divida > 0:

  juros = divida * taxa_juros 

  if divida <= pgmt_mensal:
    total_pago += divida   

  elif divida > pgmt_mensal:
    total_pago += pgmt_mensal
  
  total_juros += juros
  divida = divida + juros - pgmt_mensal
  meses += 1
 
print(f'\nTotal pago: {total_pago:.2f}\nTotal pago em juros: {total_juros:.2f}\n Quantidade de meses quitar dívida: {meses}')