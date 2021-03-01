'''

Altere o programa anterior de forma a perguntar também o valor depositado mensalmente. Esse valor será
depositado no início de cada mês, e você deve considerá-lo para o cálculo de juros do mês seguinte.

>>Questão anterior: Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma
poupança. Exiba os valores mês a mês para os 12 primeiros meses. Escreva o total ganho com juros no
período.

'''

taxa_juros = float(input("Informe o valor da taxa de juros: "))
deposito_inicial = float(input("Informe o valor do primeiro deposito: "))

taxa_juros = taxa_juros / 100

total = 0
mensal = 0

for i in range(12):
    mensal = deposito_inicial * taxa_juros
    total = mensal
    deposito_inicial = deposito_inicial + mensal
    print("O saldo do mes", i+1, "eh de: %.2f" %deposito_inicial)
    if i+1 != 12:
        deposito_mensal = float(input("Informe o valor que deseja depositar nesse mes: "))
        deposito_inicial = deposito_inicial + deposito_mensal
print("O total de ganho com os juros foi de: %.2f" %total, "R$")