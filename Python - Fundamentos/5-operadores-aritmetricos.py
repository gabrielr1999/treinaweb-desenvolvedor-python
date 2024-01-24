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

soma_idades = idade + idade2
print(f"A soma das idades é: {soma_idades}")

subtracao_idades = idade - idade2
print(f"A subtração das idades é: {subtracao_idades}")

multiplicacao_idades = idade * idade2
print(f"A mutiplicação das idades é: {multiplicacao_idades}")

media_idades = (idade + idade2) / 2
print(f"A média das idades é: {media_idades}")


# ---------------------------------------------------------------------------------------------------

# - O que são operadores aritméticos?
#   O Python dispõe de vários operadores aritméticos para a realização de cálculos matemáticos. Estes operadores 
# são utilizados para realizar operações entre dois ou mais valores, tendo sua estrutura definida da seguinte forma:
#                       variável (ou valor) [operador aritmético] variável (ou valor)
# Como dito anteriormente, o Python possui diversos operadores aritméticos, os quais podem ser vistos abaixo:
#             Operação                        Operador            Resultado

#             Adição                          +                   Soma de dois ou mais valores

#             Subtração                       -                   Subtrai dois ou mais valores

#             Multiplicação                   *                   Multiplica dois ou mais valores

#             Divisão                         /                   Divisão que retorna o valor sem arredondamento. Por exemplo, ao dividir 4/3, será retornado o valor 1,33333333

#             Exponenciação                   **                  Realiza a potência entre os valores informados

#             Parte inteira da divisão        //                  Divisão que retorna a parte inteira do resultado. Por exemplo, ao dividir 4//3, será retornado o valor 1

#             Módulo                          %                   Retorna o resto da divisão entre dois valores

# Sendo assim, abaixo temos alguns exemplos do uso dos operadores citados acima:
#                       print (10 + 10) #Resultado = 20
#                       print (10 – 5) # Resultado = 5
#                       print(10 * 5) # Resultado = 50

# - Precedência dos operadores
#   Assim como acontece na matemática, alguns operadores aritméticos possuem precedência sobre outros. Essa precedência 
# faz com que alguns cálculos tenham maior prioridade e, então, sejam executados primeiro, como no exemplo abaixo:
#                       print(10 + 2 * 4)
#   Neste caso, a multiplicação tem precedência sobre a adição, ou seja: a multiplicação será feita primeiro e seu resultado será somado com o valor 10, resultando em 18.
#   Porém, se quiséssemos que uma operação seja feita primeiro, independente de seu nível de precedência, podemos 
# utilizar os parênteses para definir a precedência, como no exemplo abaixo, onde será somado os valores 10 e 2 para então multiplicar por 4:
#                       print((10 + 2) * 4)