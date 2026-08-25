class Instituto:
     def __init__(self, organizadores, informacoes, tipo):
         self.organizadores = organizadores
         self.informacoes = informacoes
         self.tipo = tipo
     def exibir_informacoes(self):
        print(f"organizadores: {self.organizadores}, informacoes: {self.informacoes}, Tipo: {self.tipo} ")


def comprar_figurinhas():
       print("olá , quantos pacotes vc vai querer?")
       print("cada pacote custa R$ 7,00")
       quantidade = int(input("quantos? "))
       total = quantidade * 7
       if quantidade > 876:
              print(f"n temos essa quantidade somente 876 pacotes foram adicionados que deu R$ {valor},00 ")
       
    
       else:
              valor = 876 * 7
              print(f"voce comprou {quantidade} que o total deu R$ {total},00")

              a = input("o")
              if a == 1:
                     comprar_figurinhas()
