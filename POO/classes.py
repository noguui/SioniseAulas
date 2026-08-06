class Aluno: 
    #metodo construtor
    def __init__(self, nome_aluno, matricula, idade, sexo, cpf, rg, email, tel, responsaveis, endereco):
    #atributos (caracteristicas da classe/objeto)
        self.nome = nome_aluno
        self.matricula = matricula
        self.idade = idade
        self.sexo = sexo
        self.cpf = cpf
        self.rg = rg
        self.email = email
        self.telefone = tel
        self.pais = responsaveis
        self.end = endereco

class Professor:
        def __init__(self, nome_professor, siape, idade, sexo, cpf, rg, email, tel,  endereco, formacao):
            self.nome = nome_professor
            self.siape = siape
            self.idade = idade
            self.sexo = sexo
            self.cpf = cpf
            self.rg = rg
            self.email = email
            self.telefone = tel
            self.end = endereco
            self.formacao = formacao

class Televisao:
     def __init__(self, marca, tamanho, modelo):
          self.marca = marca
          self.tamanho = tamanho
          self.tamanho = modelo
class Carro:
     def __init__(self, marca, motor, modelo):
          self.marca = marca
          self.motor = motor
          self.tamanho = modelo
class Filme:
     def __init__(self, diretor, tamanho, genero):
          self.diretor = diretor
          self.tamanho = tamanho
          self.genero = genero
class Usuario:
     def __init__(self, dados, email, genero):
          self.dados = dados
          self.email = email
          self.genero = genero
class Carro:
     def __init__(self, marca, banco, modelo):
          self.marca = marca
          self.banco = banco
          self.tamanho = modelo
class Conta_Bancaria:
     def __init__(self, marca, dinheiro, opcoes):
          self.marca = marca
          self.dinheiro = dinheiro
          self.opcoes = opcoes
class Livro:
     def __init__(self, marca, paginas, opcoes):
          self.marca = marca
          self.paginas = paginas
          self.opcoes = opcoes
class Dida:
     def __init__(self, marca, sabores, temperatura ):
          self.marca = marca
          self.sabores = sabores
          self.temperatura = temperatura
class Jogo:
     def __init__(self, empresa, jogabilidade, genero):
          self.empresa = empresa
          self.jogabilidade = jogabilidade
          self.genero = genero
class Pokemon:
     def __init__(self, classe, raridade, genero):
          self.classe = classe
          self.raridade = raridade
          self.genero = genero