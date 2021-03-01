'''

Escreva um programa que exiba uma lista de opções (menu): adição, subtração, divisão, multiplicação e
sair. Imprima a tabuada da operação escolhida. Repita até que a opção "saída" seja escolhida.

'''

while(True):
    print("0. Sair")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    n = int(input("Informe a operacao: "))

    if n == 0:
        break
    else:
        op = int(input("Informe um valor: "))
        if n == 1:
            for i in range(10):
                print(i+1," + ",op," = ",(i+1)+op)
        elif n == 2:
            for i in range(10):
                print(i+1," - ",op," = ",(i+1)-op)
        elif n == 3:
            for i in range(10):
                print(i+1," * ",op," = ",(i+1)*op)
        else:
            if op == 0:
                print("Não é possivel realizar essa operacao!")
            else:
                for i in range(10):
                    print(i+1," / ",op," = ",(i+1)/op)