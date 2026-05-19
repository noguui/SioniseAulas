copa2026 = [
      {     "selecao" : "Brasil",
            "tecnico" : "Davi",
            "Goleiro": "Luke",
            "Titulos": 5
      },
      {
            "selecao" : "franca",
            "tecnico": "Didier Deschamps",
            "Goleiro": "Mike Maignan",
            "Titulos": 2
      },
      {
            "selecao" : "Portugal",
            "tecnico": "Roberto",
            "Goleiro": "Diogo Costa",
            "Titulos": 0
      }
      ]
print(copa2026) #imprime tudo

maior = copa2026[0] #inicializo com o primeiro elemento da lista

for time in copa2026:
    print("Nome da seleção: ", time["selecao"])
    print("tecnico do time:", time["tecnico"])
    print("goleiro principal", time["Goleiro"])
    print("quantidade de titulos:", time["Titulos"])
    print("============")

    if time["Titulos"] > maior["Titulos"]:
        maior = time
print("A selecao com maior titulo é: ", maior["selecao"])