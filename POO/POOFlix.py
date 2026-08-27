class Filme:
    def __init__(self, ano, diretor, classificacao, atores, sinopse, titulo, genero ):
        self.ano = ano
        self.diretor = diretor
        self.classificaçao = classificacao
        self.atores = atores 
        self.sinopse = sinopse
        self.titulo = titulo
        self.genero = genero
    def exibir_informacoes(self):
        print("\n"*3)
        print(f"----Filme---- \nAno: {self.ano}, \nDiretor: {self.diretor}, \nClassificação: {self.classificaçao},\nAtores: {self.atores}, \nSinopse: {self.sinopse}, \nTitulo: {self.titulo}, \nGenero: {self.genero}")
        print("\n"*3)

class Serie:
    def __init__(self, ano, diretor, classificacao, atores, sinopse, titulo, genero ):
        self.ano = ano
        self.diretor = diretor
        self.classificaçao = classificacao
        self.atores = atores 
        self.sinopse = sinopse
        self.titulo = titulo
        self.genero = genero
    def exibir_informacoes(self):
        print("\n"*3)
        print(f"----Serie---- \nAno: {self.ano}, \nDiretor: {self.diretor}, \nClassificação: {self.classificaçao}, \nAtores: {self.atores}, \nSinopse: {self.sinopse}, \nTitulo: {self.titulo}, \nGenero: {self.genero}")
        print("\n"*3)


class Usuario:
    def __init__(self, email, idade, cartao_bancario):
        self.email = email
        self.idade = idade
        self.cartao_bancario = cartao_bancario
    def exibir_informacoes(self):
        print("\n"*3)
        print(f"----Usuario---- \nEmail: {self.email}, \nIdade: {self.idade}, \nDados bancarios: {self.cartao_bancario} ")
        print("\n"*3)


#Instacia - Objetos
filme1 = Filme(
    "2008",
    "joao elisue",
    "9+",
    "juliao do grau e julinho do peao",
    "cawboys perdidos no espaço por causa de algo sobrenatural estranho",
    "Cawboys perdidos",
    "ação"
    )
filme1.exibir_informacoes()

serie1 = Serie(
    "2011",
    "Lola La Cava",
    "18+",
    "Castiel, Nathaniel, Lysandre, Kentin e Armin.",
    "Um estranho amor na escola",
    "Amor Doce",
    "Romance, Drama"
    )
serie1.exibir_informacoes()

usuario1 = Usuario(
    "glauberdoido@gmail.com",
    "67",
    "12345678765, 54456, 07/54, 434"
    )
usuario1.exibir_informacoes()