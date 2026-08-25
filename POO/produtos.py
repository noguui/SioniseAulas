#criar uma classe
class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade 
    #metodos da class
    def vender(self):
        pass
    def exibir(self):
        print("\n"*3)
        print(f"Nome do produto: {self.nome} ")
        print(f"Preço: R$ {self.preco}")
        print(f"Quantidade: {self.quantidade} ")
        print("\n"*3)

#Instanciar (criar um objeto)
produto1 = Produto ("Chopinho", 2.50, 10) #criei o produto
produto2 = Produto ("Açai", 13, 5)
produto3 = Produto ("Picolé", 1.50, 100)

#Atruibuindo valores ao objeto
produto2.nome = "Dida"
produto2.preco = 17
produto2.exibir()