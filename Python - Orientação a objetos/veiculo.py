class Veiculo(): # criando classe
    """ Essa é a classe veiculo. Esta classe é utilizada para instanciar novos veiculos no programa """ # docstring. Comando responsável por exibir o texto definido na docstring: help()
    def __init__(self, cor, tipo_combustivel, potencia): # definindo atributos
        self.cor = cor
        self.tipo_combustivel = tipo_combustivel
        self.potencia = potencia
        self.qtd_combustivel = 0 # possui um valor padrão
        self.is_ligado = False
        self.velocidade = 0

    def __del__(self):
        print("O objeto foi removido da memória")

    def abastecer (self, qtd_combustivel): # definindo métodos / funções
        """ O método abastecer recebe como parâmetro a quantidade de combustível e incrementa no atributo qtd_combustivel do objeto veículo """
        self.qtd_combustivel += qtd_combustivel

    def ligar(self):
        if self.is_ligado:
            print("O veículo já está ligado")
        else:
            self.is_ligado = True
            print("O veículo foi ligado")

    def desligar(self):
        if self.is_ligado == False:
            print("O veículo já está desligado")
        else:
            self.is_ligado = False
            print("O veículo foi desligado")

    def acelerar(self, velocidade=10):
        if self.is_ligado:
            self.velocidade += velocidade
        else:
            print("O veículo precisa estar ligado para ser acelerado")