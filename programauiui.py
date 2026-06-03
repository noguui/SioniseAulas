#tres numeros , com soma , ordem crescente , verificar qual sao par e impar, informar o dobro e metade
 
def soma():
    soma = n1 + n2 + n3
    print(soma)
def crescente():
    eae = [n1,n2,n3]
    eae.sort()
    print(eae)
def impar_par():
    if n1 % 2 == 0:
        print(f"{n1} é PAR")
    else:
        print(f"O {n1} é IMPAR")
    if n2 % 2 == 0:
        print(f"O {n2} é PAR")
    else:
        print(f"O {n2} é IMPAR")
    if n3 % 2 == 0:
        print(f"O {n3} é PAR")
    else:
        print(f"O {n3} é IMPAR")
def multiplicaçao():
    print(n1*2)
    print(n2*2)
    print(n3*2)
def divisão():
    print(n1/2)
    print(n2/2)
    print(n3/2)
def sair():
    print("flw")

n1 = int(input("o primeiro numero:"))
n2 = int(input("o segundo numero: "))
n3 = int(input("o terceiro numero:"))
while True:
    print("escolha tres numeros que mostraremos a soma deles, a ordem crescente , se é impar ou par e o dobro e a metade dele")
    opção1 = print("1 - soma")
    opção2 = print("2 - crescente")
    opção3 = print("3 - impar ou par")
    opção4 = print("4 - dobro")
    opção5 = print("5 - metade")
    opção6 = print("6 - sair")
    p1 = int(input("qual vc quer?: "))
    if p1 == 1:
        soma()
    elif p1 == 2:
        crescente()
    elif p1 == 3:
        impar_par()
    elif p1 == 4:
        multiplicaçao()
    elif p1 == 5:
        divisão()
    elif p1 == 6:
        sair()
        break
    else:
        print("opçao invalida")