class Sala:
    def __init__(self,cadeira, quadro, alunos ):
        self.cadeira = cadeira
        self.quadro  = quadro
        self.alunos = alunos
    def exibir_informacoes(self):
        print(f"oque tem nela: {self.cadeira}, a coisa mais importante: {self.quadro}, alunos: {self.alunos}")
Sala1 = Sala(
    "cadeira",
    "quadro",
    "julio e felipe "
    )
Sala1.exibir_informacoes()
class Cinema:
    def __init__(self, filme, tela, pessoas):
        self.filme = filme
        self.tela = tela
        self.pessoas = pessoas
    def exibir_informacoes(self):
        print(f"filme: {self.filme}, tela: {self.tela}, quantidade : {self.pessoas}")
Cinema1 = Cinema(
    "sonic",
    "155 polegadas",
    "70 pessoas"
)
Cinema1.exibir_informacoes()
class Bicicleta:
    def __init__ (self, roda, corrente, quadro):
        self.roda = roda
        self.corrente = corrente
        self.quadro = quadro
    def exibir_informacoes(self):
        print(f"roda: {self.roda}, corrente: {self.corrente}, quadro: {self.quadro}")
Bicicleta1 = Bicicleta(
    "33 cm",
    "yamaha",
    "muito"
)
Bicicleta1.exibir_informacoes()
class Roupa:
    def __init__(self, material, tamanho):
        self.material = material
        self.tamanho = tamanho
    def exibir_informacoes(self):
        print(f"material: {self.material}, tamanho: {self.tamanho}")
roupa1 = Roupa(
    "algodao",
    "M"
)
roupa1.exibir_informacoes()
class Cerveja:
    def __init__ (self, alcool, cevada, marca ):
            self.alcool = alcool
            self.cevada = cevada 
            self.marca = marca
    def exibir_informacoes(self):
        print(f"alcool: {self.alcool}, cevada: {self.cevada}, marca: {self.marca}")
cerveja1 = Cerveja(
    "10%",
    "5%",
    "brahma"
)
cerveja1.exibir_informacoes()
class Instituto:
    def __init__(self, organizadores, informacoes, tipo):
        self.organizadores = organizadores
        self.informacoes = informacoes
        self.tipo = tipo
    def exibir_informacoes(self):
        print(f"Organizadores: {self.organizadores}, Informações: {self.informacoes}, Tipo: {self.tipo}")


instituto1 = Instituto(
    "Guilherme e Luana",
    "Evento de tecnologia",
    "Palestra"
)

instituto1.exibir_informacoes()