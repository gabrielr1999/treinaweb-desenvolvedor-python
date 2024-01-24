class Usuario:
    def __init__(self, nome, idade, sobrenome):
        self.nome = nome
        self.idade = idade
        self.sobrenome = sobrenome
        
# ----------------------------------------------------------------------------------------------------------------------------------------------

#   - Como funcionam os módulos no Python
#       Ao trabalhar com orientação a objetos, percebemos a necessidade de separar e organizar nosso código. No Python, as classes são criadas em arquivos separados 
#   para melhorar o poder de reaproveitamento em nosso software. Cada arquivo representa um módulo em nosso programa. Estes módulos podem ser importados por outros 
#   módulos e, assim, utilizar os atributos ou métodos definidos entre os arquivos.
#       No Python, para importar módulos entre arquivos, utilizamos dois comandos:  
#           - import: importa o módulo por completo;
#           - from: importa apenas parte do módulo.
#       Por exemplo: imagine que possuímos dois arquivos em nosso projeto. Uma classe Pessoa (com todos os seus atributos) e um arquivo main, responsável por instanciar 
#   os objetos do tipo Pessoa. Porém, sem a importação do módulo Pessoa, o arquivo main não consegue visualizar e instanciar a classe Pessoa. Para isso, devemos importar a 
#   classe Pessoa e, assim, instanciar a classe:
        
#                               #classe Pessoa
#                               class Pessoa:
#                                   def __init__(self, nome, idade, sexo):
#                                       self.nome = nome
#                                       self.idade = idade
#                                       self.sexo = sexo
#                               #classe main
#                               from pessoa import Pessoa
#                               pessoa1 = Pessoa("Maria", 25, "Feminino")
#                               print(pessoa1.nome)
#                               print(pessoa1.idade)
#                               print(pessoa1.sexo)


