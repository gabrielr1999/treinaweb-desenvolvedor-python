from usuario import Usuario

continuar = 1
lista_usuarios = []

while continuar!= 0:
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    sobrenome = input("Digite seu sobrenome: ")

    usuario = Usuario(nome, idade, sobrenome)
    lista_usuarios.append(usuario)

    if usuario.idade == 99:
        break
    if usuario.idade == 98:
        continue

    print(f"Olá, {usuario.nome} {usuario.sobrenome}, sua idade é {usuario.idade}")

    if usuario.idade <= 17:
        print(f"{usuario.nome} é adolecente")
    elif usuario.idade >= 18 and usuario.idade <= 50:
        print(f"{usuario.nome} é adulto")
    else:
        print(f"{usuario.nome} é idoso") 

    continuar = int(input("Deseja continuar cadastrando? 0 - Sair 1 - Continuar"))
else:
    print("Lista de usuários cadastrados: ")

    for x in lista_usuarios:
        print(f"Nome Completo: {x.nome} {x.sobrenome} - Idade {x.idade}")

    print("o loop entrou no else")

# ----------------------------------------------------------------------------------------------------------------------------------------------
#   - Desafio do código #1
#       Supondo três inteiros: a, b e n, aplicados a seguinte fórmula:
#           (a + 20 x b),(a + 20 x b + 21 x b), ... , (a + 20 x b + 21 x b + ... + 2n-1 x b)
#       Onde serão informados q sequências de a, b e n. Para cada uma, informe no console a série correspondente dos valores em uma única linha, separados por espaço.

#   + Explicação:

#       Sendo passado duas sequências:

#       1°: Onde a = 0, b = 2 e n = 3, é produzido os dados:

#               0 + 1 x 2 = 2
#               0 + 1 x 2 + 2 x 2 = 6
#               0 + 1 x 2 + 2 x 2 + 4 x 2 = 14

#       2°: Onde a = 5, b = 3 e n = 5, é produzido os dados:

#               5 + 1 x 3 = 8
#               5 + 1 x 3 + 2 x 3 = 14
#               5 + 1 x 3 + 2 x 3 + 4 x 3 = 26
#               5 + 1 x 3 + 2 x 3 + 4 x 3 + 8 x 3 = 50
#               5 + 1 x 3 + 2 x 3 + 4 x 3 + 8 x 3 + 16 x 3 = 98

#       Obs: No Python utilize a função pow para potenciação e o parâmetro end para exibir um valor com o print sem gerar uma nova linha.
  
#   Resposta:
    
#                           t = int(input())
#                           for i in range(0,t):
#                               a, b, n = input().split()
            
#                               result = []
#                               for j in range(0,int(n)):
#                                   result.insert(j, int(a))
    
#                                   for k in range(0,j+1):
#                                       exp = pow(2, k)
#                                       result[j] += exp * int(b);
                
#                               for r in result:
#                                   print(r, end = ' ')
            
#                               print('')

#   - Desafio do código #2
#       Considerando uma lista (lista = []), você pode executar as ações:

#           1 - insert i e: Inserir o inteiro e na posição i;
#           2 - print: Exibe a lista;
#           3 - remove e: Exclui a primeira ocorrência do inteiro e;
#           4 - append e: Adiciona o inteiro e no final da lista;
#           5 - sort: Ordena a lista;
#           6 - pop: Remove o último elemento da lista;
#           7 - reverse: Inverte a lista.
#       Onde serão informadas N sequências de ações da listagem acima, que devem ser aplicadas em uma lista.
#                                n = int(input())
#
#                                lista = []
#                                for i in range(0, n):
#                                    values = input().split()

#                                    if len(values) == 3:
#                                        acao, i, e = values
#                                    elif len(values) == 2:
#                                        acao, e = values
#                                    else:
#                                        acao = values.pop()
#                                    
#                                    if acao == "insert":
#                                        lista.insert(int(i), int(e))
#                                    elif acao == "print":
#                                        print(lista)
#                                    elif acao == "remove":
#                                        lista.remove(int(e))
#                                    elif acao == "append":
#                                        lista.append(int(e))
#                                    elif acao == "sort":
#                                        lista.sort()
#                                    elif acao == "pop":
#                                        lista.pop()
#                                    elif acao == "reverse":
#                                        lista.reverse()

# ----------------------------------------------------------------------------------------------------------------------------------------------

#   - O que são as listas e como funcionam
#       Uma lista é uma estrutura de dados representada como uma sequência de objetos separados por vírgula, podendo armazenar qualquer tipo de dado e ser 
#   alterada a qualquer momento.
#       Para declarar uma lista no Python, utilizamos a seguinte sintaxe:

#                               nome_da_lista = [elemento1, elemento2, elemento3]

#       No Python, podemos utilizar diversos métodos para manipular as listas, como veremos alguns destes abaixo.

#       Para inserir novos elementos em uma lista, utilizamos o método append(). Este método irá inserir determinado elemento ao final da lista em questão:

#                               lista = ["Arroz", "Feijão"]
#                               lista.append("Macarrão")
#                               print(lista) #Arroz, Feijão, Macarrão

#       Para inserir elementos em uma determinada posição de uma lista, utilizamos o método insert(). Este método recebe como parâmetro o elemento a ser inserido e sua posição:

#                               lista = ["Arroz", "Feijão"]
#                               lista.insert(1, "Macarrão")
#                               print(lista) #Arroz, Macarrão, Feijão

#       Para remover elementos de uma lista, utilizamos o método remove(). Este método recebe como parâmetro o elemento a ser removido:

#                               lista = ["Arroz", "Feijão"]
#                               lista.insert(1, "Macarrão")
#                               print(lista) #Arroz, Macarrão, Feijão
#                               lista.remove("Macarrão")
#                               print(lista) #Arroz, Feijão

#       Além dos métodos citados acima, o Python dispõe de outros meios para manipularmos listas:
#           - pop(índice): remove o elemento da lista;
#           - index(elemento): retorna o índice do elemento na lista;
#           - count(elemento): retorna a quantidade de vezes em que um elemento aparece na lista;
#           - sort(): ordena a lista;
#           - reverse(): inverte a ordem da lista.
















