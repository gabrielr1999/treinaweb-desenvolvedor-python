nome, idade, sobrenome = "João", 20 , "Silva"

print(f"Olá, {nome} {sobrenome}, sua idade é {idade}")

if idade >= 18:
    print(f"{nome} é maior de idade")
else:
    print(f"{nome} é menor de idade")

nome2 = input("Digite seu nome: ")
idade2 = int(input("Digite sua idade: "))
sobrenome2 = input("Digite seu sobrenome: ")

print(f"Olá, {nome2} {sobrenome2}, sua idade é {idade2}")

media_idades = (idade + idade2) / 2
print(f"A média das idades é: {media_idades}")

if idade2 <= 17:
    print(f"{nome2} é adolecente")
elif idade2 >= 18 and idade2 <= 50:
    print(f"{nome2} é adulto")
else:
    print(f"{nome2} é idoso") 

# ----------------------------------------------------------------------------------------------------------------------------------------------
# 
#   - Desafio de código 1
#   Dado um valor inteiro N, complete o código abaixo de acordo com as condições:
#       + Se N for par, exiba no console: "Par";
#       + Se N for ímpar, exiba no console: "Ímpar".
#                   n = int(input())
#                   if n % 2 == 0:
#                       print("Par")
#                   else:
#                       print("Ímpar")

#   - Desafio de código 2
#   Dado um valor inteiro N, complete o código abaixo de acordo com as condições:
#       + Se N for ímpar, exiba no console: "Estranho";
#       + Se N for par e for menor que 10, exiba no console: "Não é estranho";
#       + Se N for par e estiver entre 10 e 20, exiba no console: "Estranho";
#       + Se N for par e for maior que 20, exiba no console: "Não é estranho".
#                   n = int(input())
#                   if n % 2 != 0:
#                       print("Estranho")
#                   elif n < 10:
#                       print("Não é estranho")
#                   elif n >= 10 and n <=20:
#                       print('Estranho')
#                   else:
#                       print("Não é estranho") 

# ----------------------------------------------------------------------------------------------------------------------------------------------

#   - O que são operadores lógicos?
#   Os operadores lógicos são responsáveis por testar se uma determinada comparação entre dois ou mais valores são verdadeiros.
#   Por exemplo: imaginemos que é necessário verificar qual paciente possui idade menor ou igual a 10 anos para que este seja encaminhado com 
# urgência diferenciada em relação aos outros. Para isso, utilizamos operadores que irão comparar a idade deste paciente e retornar verdadeiro se a 
# condição for satisfeita ou falso se a condição não for satisfeita.
#   No Python, possuímos diversos operadores lógicos, como podem ser vistos abaixo:
#                   Operador       Operação
#                   <              Menor
#                   >              Maior
#                   <=             Menor ou igual
#                   >=             Menor ou igual
#                   ==             Igual
#                   ==             Diferente
#
#   - Condicional if-else e if-elif-else
#   Para avaliar a veracidade de uma expressão booleana, utilizamos os comandos if e else. O if irá verificar se 
# determinada condição é verdadeira e executará determinado bloco de código. Caso a expressão não for verdadeira, será executado o bloco do comando else; 
# comando este que, por sua vez, irá executar outro bloco de código.
#                   
#                   if (condição):
#                       <bloco de código>
#                   else:
#                       <bloco de código>
# 
#   Sendo assim, utilizamos os condicionais if e else para testar uma única expressão booleana, como no exemplo a seguir:
# 
#                   idade = 10
#                   if (idade <= 10):
#                       print("O paciente tem prioridade")
#                   else:
#                       print("O paciente deve aguardar atendimento")
# 
#   Porém, com base no exemplo acima, como faríamos para adicionar uma prioridade maior que os pacientes que possuem idade maior que 10 e uma prioridade menor 
# aos pacientes menores que 10 anos? E isso tudo sendo necessário adicionar um nível maior de prioridade aos pacientes idosos... Para isso, podemos utilizar o 
# condicional elif. Este condicional irá verificar uma outra expressão booleana, caso a condição definida no if não seja satisfeita:
#
#                   idade = 10
#                   if (idade <= 10):
#                       print("O paciente tem prioridade")
#                   elif (idade >= 60):
#                       print("O paciente tem prioridade nível dois")
#                   else:
#                       print("O paciente deve aguardar atendimento")
#   - Atribuição condicional
#   Também é possível definir o valor de uma variável a depender do resultado de uma condição lógica, como podemos ver abaixo: 
#   
#                   prioridade = "Prioridade 1" if (idade <= 10) else "Prioridade 2"
#
#