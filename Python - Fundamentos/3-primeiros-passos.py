### 3 - Primeiros passos com Python ###

nome = "João"
idade = 25
sobrenome = "Silva"

print(nome, sobrenome, idade)

print("Olá,", nome, sobrenome, "sua idade é", idade) #forma convencional
print(f"Olá, {nome} {sobrenome}, sua idade é {idade}")

# Capturando dados do teclado
nome2 = input("Digite seu nome: ")
idade2 = int(input("Digite sua idade: ")) # convertendo uma string para um tipo inteiro
sobrenome2 = input("Digite seu sobrenome: ")

print(type(idade2))

print(f"Olá, {nome2} {sobrenome2}, sua idade é {idade2}")