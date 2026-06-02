#tres numros , com soma , ordem crescente , verificar qual sao par e impar, informar o dobro e metade

def soma():
    soma = n1 + n2 + n3
    print(soma)
def crescente():
    eae = [n1,n2,n3]
    eae.sort()
    print(eae)
def impar_par():
    if n1 % 2 == 0:
        print("O numero é PAR")
    else:
        print("O numero é IMPAR")
    if n2 % 2 == 0:
        print("O numero é PAR")
    else:
        print("O numero é IMPAR")
    if n3 % 2 == 0:
        print("O numero é PAR")
    else:
        print("O numero é IMPAR")
def multiplicaçao():
    print(n1*2)
    print(n2*2)
    print(n3*2)
def divisão():
    print(n1/2)
    print(n2/2)
    print(n3/2)

print("escolha tres numeros que mostraremos a soma deles , se é impar ou par e o dobro e a metade dele")
n1 = int(input("o primeiro numero:"))
n2 = int(input("o segundo numero: "))
n3 = int(input("o terceiro numero:"))

soma()
crescente()
impar_par()
multiplicaçao()
divisão()