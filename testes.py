dicionario = {"nome": "Ana", "idade": 25}

chave = input("Digite o nome da chave a consultar: ")

if chave in dicionario:
    print(f"Ok! A chave '{chave}' existe e o valor é: {dicionario[chave]}")
else:
    print(f"Não existe a chave '{chave}' no dicionário.")   

p3 = input("Qual sabor você quer? ").strip().lower()
    item_encontrado = None
    for item in loja:
        if item["sabor"] == p3:
            item_encontrado = item

            loja = [
    {"sabor": "morango", "preço": 5, "quantidade": 22},
    {"sabor": "chocolate", "preço": 5, "quantidade": 44},
    {"sabor": "uva", "preço": 5, "quantidade": 21}
]

print("Nossos sabores:", [item["sabor"] for item in loja])

loja = [
 {          "sabor" : "morango",
            "preço" : 5,
            "quantidade": 22,
      },
      {
            "sabor" : "chocolate",
            "preço" : 5,
            "quantidade": 44,
      },
      {
            "sabor" : "uva",
            "preço" : 5,
            "quantidade": 21,
      }
]
print(loja)

while True:
    p1 = input("Você deseja comprar?: ")
    if p1 == "nao":
        break
    if p1 == "sim":
        p2 = input("Quer continuar? : ")
        if p2 == "nao":
            break 
        if p2 == "sim":
            p3 = input("Qual sabor você quer? ")
            algum_item = None
            for item in loja:
                if item["sabor"] == p3:
                    algum_item = item
                    break 
            if algum_item is not None:
                p4 = int(input("Quantas unidades você deseja? "))      
                if p4 <= algum_item["quantidade"]:
                    total = p4 * algum_item["preço"]
                    print(f"Você comprou {p4} unidades de {p3}. Total: R$ {total:.2f}")
                    print("obrigado")
                    break
        else:
            print(f"fez algo errado")

def comprar_album():
    print("1 - Capa mole - R$ 15,00")
    print("2 - Capa dura - R$ 25,00")
    print("3 - Capa gold - R$ 40,00")

    qual_album = int(input("Qual opção você deseja? "))

    if qual_album == 1:
        quantidade = int(input("Quantos? "))
        total = quantidade * 15
        print(f"Você comprou {quantidade} álbum(ns) e o total deu R$ {total},00")

    elif qual_album == 2:
        quantidade = int(input("Quantos? "))
        total = quantidade * 25
        print(f"Você comprou {quantidade} álbum(ns) e o total deu R$ {total},00")

    elif qual_album == 3:
        quantidade = int(input("Quantos? "))
        total = quantidade * 40
        print(f"Você comprou {quantidade} álbum(ns) e o total deu R$ {total},00")

    else:
        print("Opção inválida")