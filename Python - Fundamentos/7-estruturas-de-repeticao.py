nome, idade, sobrenome = "João", 20 , "Silva"

for x in range(1, 10):
    print(f"Olá, {nome} {sobrenome}, sua idade é {idade}")

    if x ==2:
        continue
    if x == 8:
        break

    print(x)

    if idade >= 18:
        print(f"{nome} é maior de idade")
    else:
        print(f"{nome} é menor de idade")
else: 
    print("O loop entrou no else")

idade2 = 1
while idade2!= 0:
    nome2 = input("Digite seu nome: ")
    idade2 = int(input("Digite sua idade: "))
    sobrenome2 = input("Digite seu sobrenome: ")

    if idade2 == 99:
        break
    if idade2 == 98:
        continue

    print(f"Olá, {nome2} {sobrenome2}, sua idade é {idade2}")

    media_idades = (idade + idade2) / 2
    print(f"A média das idades é: {media_idades}")

    if idade2 <= 17:
        print(f"{nome2} é adolecente")
    elif idade2 >= 18 and idade2 <= 50:
        print(f"{nome2} é adulto")
    else:
        print(f"{nome2} é idoso") 
else:
    print("o loop entrou no else")

# ----------------------------------------------------------------------------------------------------------------------------------------------

#   - Desafio de código 1
#       Exiba todas os números pares

#                   for x in range(1, 10):
#                       if x % 2 == 0:
#                           print(x)
#   - Desafio de código 2
#       Seja lido um valor N e seja retornado o seu valor fatorial.

#                   n = int(input())
#                   resultado=1
#                   count=1

#                   while count <= n:
#                       resultado *= count
#                       count += 1
#                   print(resultado)

#   ou 

#                   fatorial = 1
        
#                   for x in range(1, n+1):
#                       fatorial = fatorial * x  
#                   print(fatorial)

#   - Desafio do código 3
#       Receba um número e faça sua tabuada
#       
#                   N = int(input())
#                   for count in range(10):
#                       print("%d x %d = %d" % (N, count+1, N*(count+1)) )

# ou

#                   for i in range(1, 11):
#                       print("{} x {} = {}".format(N, i, N * i))


# ----------------------------------------------------------------------------------------------------------------------------------------------

#   - O que são estruturas de repetição?
#       Uma estrutura de repetição é responsável por permitir que um determinado bloco de código seja executado diversas vezes, até que uma determinada condição 
#   seja atendida. No Python, possuímos duas estruturas de repetição:

#               + While
#               + For

#   - While
#       O while é uma estrutura de repetição que permite executar um determinado bloco de código enquanto uma determinada condição seja satisfeita. Ela é muito utilizada 
#   quando não se sabe o número de iterações que devem ser feitas.
#       O while possui a seguinte sintaxe no Python:

#             while (condição):
#                 <bloco de código>

#       Um exemplo deste comando pode ser visto abaixo:

#               numero = 0
#               soma = 0
#               while numero < 20:
#                   numero = int(input("Digite um número menor que 20. Ou maior para finalizar o laço"))
#                   soma = soma + numero
#               print(soma)

#   - For
#       Diferente do while, o for executa um determinado bloco de código por uma determinada quantidade de vezes, quantidade de vezes esta que é indicada em sua declaração. 
#   Estrutura de repetição mais utilizada no Python, o for tem sua sintaxe definida da seguinte forma:
    
#               for variável_referencia in sequencia:
#               <bloco de código>

#       Para determinar a sequência do laço, a função range é muito utilizada no Python. Ela retorna uma lista de inteiros em um determinado intervalo, como pode ser visto abaixo:

#               for x in range(1, 1):
#                    y = x + 1
#               print(y) #10

#   - For-else e While-else
#       O Python disponibiliza o comando else para definir um bloco de código que será executado imediatamente após o fim de um loop. Por exemplo: imagine que queremos 
#   informar ao usuário que o loop foi encerrado ao final do seu ciclo de execução. Para isso, utilizamos o else, conforme exemplo abaixo:

#               for x in range(1, 10):
#                   y = x + 1
#               else:
#                   print("loop encerrado com sucesso")
#               print(y) #10

#       Vale lembrar que o comando else pode ser usado também no while:

#               numero = 0
#               soma = 0
#               while numero < 20:
#                   numero = int(input("Digite um número menor que 20"))
#                   soma = soma + numero
#               else:
#                   print("loop encerrado com sucesso")
#               print(soma)

#   - Break
#       É comum que, em certas situações, queiramos abortar a execução de um loop a depender de uma certa condição... Para isso, utilizamos o comando break. O break 
#   vai encerrar a execução do bloco de código imediatamente ao ser chamado:

#               numero = 0
#               soma = 0
#               while numero < 20:
#                   numero = int(input("Digite um número menor que 20"))
#                   if numero == 16:
#                       break
#                   soma = soma + numero
#               print(soma)

#   - Continue
#       Por outro lado, é comum que queiramos ignorar a execução de um passo do loop quando uma determinada condição é satisfeita. Para isso, utilizamos o comando continue:

#               numero = 0
#               soma = 0
#               while numero < 20:
#                   numero = int(input("Digite um número menor que 20"))
#                   if numero == 16:
#                       continue
#                   soma = soma + numero
#               print(soma)

#       O comando acima irá "saltar" a execução quando o numero em questão for 16.




