def comprar_figurinhas():
       print("olá , quantos pacotes vc vai querer?")
       print("cada pacote custa R$ 7,00")
       quantidade = int(input("quantos? "))
       total = quantidade * 7
       print(f"voce comprou {quantidade} que o total deu R$ {total},00")

def comprar_album():
       print("1 - Capa mole - R$ 15,00")
       print("2 - Capa dura - R$ 25,00")
       print("3 - Capa gold - R$ 40,00")
       print("olá , quantos albuns vc vai querer?")
       qual_album = input("qual opçao vc deseja? ")
       print("cada pacote custa R$ 15,00")
       quantidade = int(input("quantos? "))
       total = quantidade * 15
       print(f"voce comprou {quantidade} que o total deu R$ {total},00")

       elif qual_album == 2:
       quantidade = int(input("quantos? "))
       total = quantidade * 25
       print(f"voce comprou {quantidade} que o total deu R$ {total},00")

       if qual_album == 3:
               quantidade = int(input("quantos? "))
       total = quantidade * 40
       print(f"voce comprou {quantidade} que o total deu R$ {total},00")

def entrar_grupo():
        print("Entre no nosso grupo de figurinhas e fique por dentro de todas as novidades!" \
        " Lá você encontra figurinhas divertidas, conteúdos exclusivos e ainda participa de" \
        " um espaço cheio de interação e entretenimento.")
        deseja_entrar = input("voce deseja entrar no grupo? (S/N): ").upper()
        if deseja_entrar == "S":
                print("obrigado por entrar, voce nao ira se arrepender")
                nome = input("nome: ")
                telefone = input("telefone: ")
                caso_entrou_no_grupo.append({
                "nome": nome,
                "telefone": telefone
                        })
        elif deseja_entrar == "N":
                print(":(")
        else:
                print("opçao invalida")
def sair():
        print("ate depois, volte logo sentimos a sua falta")

caso_entrou_no_grupo = []
while True:
    print("Bem vindo a loja de vendas de figurinhas da Copa. Escolha uma das opçoes abaixo:")
    print("1 - Comprar pacotes de figurinhas")
    print("2 - Comprar album")
    print("3 - Entrar no grupo de figurinha")
    print("4 - sair do programa")

    p1 = int(input("qual o numero vc quer? "))

    if p1 == 1:
           comprar_figurinhas()    
    elif p1 == 2:
        comprar_album()
    elif p1 == 3:
           entrar_grupo()
    elif p1 == 4:
           sair()
           break
    else:
        print("opção invalida")