import carro
import moto

uno_vermelho = carro.Carro("vermelho", "Flex", 1.0, 4)
# help(uno_vermelho.abastecer)
uno_vermelho.ligar()
uno_vermelho.abastecer(100)
uno_vermelho.abastecer(100)
uno_vermelho.abastecer(20)
print(f"A quantidade de combustível do veículo é: {uno_vermelho.qtd_combustivel}")
del uno_vermelho

moto_vermelha = moto.Moto("vermelho", "Gasolina", 1.0, 2)
moto_vermelha.ligar()
print(moto_vermelha.is_ligado)

# uno_preto = carro.Carro("preto", "2", "Flex", 1.4)
# uno_preto.desligar()
# print(f"A quantidade de combustível do veículo é: {uno_preto.qtd_combustivel}")
# uno_preto.acelerar(20)
# uno_preto.ligar()
# uno_preto.acelerar()
# print(f"A velocidade do veículo é: {uno_preto.velocidade}")
