'''
6) Modifique o programa anterior de forma que o usuário também digite o início e o fim da tabuada, em vez de começar com 1 e 10.

n = int(input("Tabuada de: "))
x = 1
while x <= 10:
	print(x ,"x", n ,"=" , n * x)
	x = x + 1
'''

inicio = int(input("Informe o inicio da tabuada: "))
fim = int(input("Informe o final da tabuada: "))
n = int(input("Tabuada de: "))

while inicio <= fim:
	print(inicio ,"x", n ,"=" , n * inicio)
	inicio += 1