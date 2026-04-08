# Programa: Lista com dobro e triplo

original = []
modificada = []

print("Digite 30 números inteiros:")
for i in range(30):
    numero = int(input(f"numero {i+1}: "))
    original.append(numero)

for i in range(30):
    valor_atual = original[i]
    
    if i % 2 == 0:
        novo_valor = valor_atual * 2
    else:
        novo_valor = valor_atual * 3
        
    modificada.append(novo_valor)

print("Lista Original:", original)
print("Lista Modificada:", modificada)
