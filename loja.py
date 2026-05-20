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
    if p1 == 'nao': 
        print("Até a próxima!")
        break    
    if p1 == 'sim': 
        p2 = input("Quer continuar? : ")
        if p2 == 'nao': 
            print("Até a próxima!")
            break        
        if p2 == 'sim': 
            p3 = input("Qual sabor você quer? ")
            algum_item = None        
            for item in loja: 
                if item['sabor'] == p3: 
                    algum_item = item 
                    break                
            if algum_item is not None: 
                p4 = int(input("Quantas unidades você deseja? "))
                if p4 <= algum_item['quantidade']: 
                    total = p4 * algum_item['preço'] 
                    print(f"Você comprou {p4} unidades de {p3}. Total: R$ {total:.2f}") 
                else: 
                    print("Estoque insuficiente")