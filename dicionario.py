pessoa = {
    "nome": "Guilherme",
    "idade": 16,
    "sexo": "Masculino"
}
print(pessoa)

for chave, valor in pessoa.items():
    print(f"{chave} é {valor}")

for chave in pessoa.keys():
    print(f'A chave é {chave}')
for valor in pessoa.values():
    print(f'O valor da chave é {valor}')

#fim da aula