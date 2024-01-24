### 4 - Operadores de atribuição ###

nome, idade, sobrenome = "João", 20 , "Silva"

print(nome, sobrenome, idade)

print("Olá,", nome, sobrenome, "sua idade é", idade) #forma convencional
print(f"Olá, {nome} {sobrenome}, sua idade é {idade}")

# Capturando dados do teclado
nome2 = input("Digite seu nome: ")
idade2 = int(input("Digite sua idade: ")) # convertendo uma string para um tipo inteiro
sobrenome2 = input("Digite seu sobrenome: ")

print(type(idade2))

print(f"Olá, {nome2} {sobrenome2}, sua idade é {idade2}")

nome3, telefone, email = "João" "joao@mail.com", "123456" # Vai dar erro de compilação

# Exercício
linguagem, nivel, companhia = input().split() # Sabendo que os dados obtidos pela função input(), podem ser convertidos para array com a função split()

print(linguagem)
print(nivel)
print(companhia)

# ---------------------------------------------------------------------------------------------------

#O que são operadores de atribuição?
#  A atribuição é a forma em que se define um valor referente à determinada variável. No Python, como em várias outras 
# linguagens de programação, a atribuição é dada da seguinte forma: a variável à esquerda recebe o valor definido à direita, 
# sendo separado pelo sinal de igual ( = ), como pode ser visto abaixo:
#                                               X = 10
#  Por possuir tipagem dinâmica, não é necessário definir o tipo da variável que é criada no Python, essa informação será definida a 
# partir do valor que a variável recebe. Por exemplo, se uma variável recebe um valor inteiro, logo seu tipo será int; já uma variável que 
# recebe uma cadeia de caracteres terá seu tipo definido como string.
#
#  No Python, para descobrir o tipo de uma variável, utilizamos o método type, como pode ser visto no código abaixo:
#                                               x = 10
#                                               y = "Teste"
#                                               print(type(x))
#                                               print(type(y))