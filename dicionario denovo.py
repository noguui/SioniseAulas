aluno = {
    "nome" : "Guilherme",
    "data_nascimento" : "24/08/2009",
    "cpf" : 148,
    "rg" : 64,
    "telefone" : 8199
}
alunos = [
    { "nome" : "Guilherme",
    "data_nascimento" : "24/08/2009",
    "cpf" : 148,
    "rg" : 64,
    "telefone" : 8165
    },
    { "nome" : "Silvio",
    "data_nascimento" : "26/07/2005",
    "cpf" : 140,
    "rg" : 67,
    "telefone" : 81876
    },
    { "nome" : "Felipe",
    "data_nascimento" : "12/03/2007",
    "cpf" : 134,
    "rg" : 61,
    "telefone" : 8143
    }
]
print(alunos) #imprime tudo 
print("===============")
print(alunos[2]) #imprime so o 2
print("===============")
print(alunos[2]["nome"]) #imprime so o nome do 2
print("===============")
print(alunos[0]["telefone"]) #imprime so o telefone do 0 