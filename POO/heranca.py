
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def exibir_dados(self):
        print(f" nome: {self.nome}, idade: {self.idade}")

class Professor(Pessoa):
    pass
class Aluno(Pessoa):
    pass
class TAE(Pessoa):
    pass

#instanciar objetos
aluno1 = Aluno("Maria", 30)
aluno2 = Aluno("José", 67)
prof1 = Professor("Sionise", 42)
prof2 = Professor ("Josiel", 47)
tae = TAE("gil", 34)
tae2 = TAE("Rosa", 87)
#chamada dos metodos
aluno1.exibir_dados()
aluno2.exibir_dados()
prof1.exibir_dados()
prof2.exibir_dados()
tae.exibir_dados()
tae2.exibir_dados()