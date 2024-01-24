class Usuario:
    def __init__(self, nome, idade, sobrenome):
        self.nome = nome
        self.idade = idade
        self.sobrenome = sobrenome
        
# ----------------------------------------------------------------------------------------------------------------------------------------------

#   - O que é Orientação à Objetos?
#       Orientação a Objetos é um paradigma de programação baseado no conceito de "objetos". Estes objetos representam um indivíduo ou coisa existente 
#   "de verdade" em nosso mundo, fazendo com que a programação se torne o mais próximo do mundo real possível.
#       As classes definem a estrutura de cada objeto, ou seja, quais atributos (campos) e métodos (comportamentos) os objetos possuirão. Podemos então considerar uma classe 
#   como um molde de uma representação do mundo real.
#       Já os objetos constituem uma "cópia" deste molde, ou seja, uma representação de uma classe.
#       Por exemplo: imagine que possuímos uma classe que representa uma pessoa no mundo real. Esta classe irá definir os atributos desta pessoa 
#   (nome, idade e sexo); porém, sabemos que as informações de cada pessoa variam... Sendo assim, para cada pessoa que formos criar em nosso software, devemos 
#   instanciar um novo objeto. Desta forma, conseguimos criar um objeto com suas determinadas características.
#       O que são as classes?
#       Uma classe é a representação de um elemento do mundo real a ser reproduzido em um software. Por exemplo, imagine o carro da imagem abaixo:

#                                                   ********** imagem do carro ************

#       É fácil perceber que todo carro possui características em comum, como:
#   - Cor;
#   - Quantidade de portas;
#   - Tipo de combustível;
#   - Acessórios;
#   - Etc.

#       Sendo assim, uma classe irá definir a estrutura básica de um carro, onde será criada uma classe Carro, e dentro dessa classe, definido as características 
#   de um carro. Ou seja, sempre que quisermos definir a estrutura padrão de algum objeto da vida real em um software, criamos uma classe para este objeto.
#   - O que são objetos?
#       Objetos são a representação de uma classe. No último tópico vimos que as classes determinam a estrutura básica de um elemento da vida real e utilizamos como exemplo 
#   um carro. Sabemos que há vários tipos de carros, porém eles possuem uma estrutura básica similar, definida em sua classe. Ou seja, uma classe pode ser considerada 
#   como um molde de objetos.
#       Se quisermos criar um novo carro, simplesmente utilizamos sua classe e definimos seus atributos. Essa utilização da classe é chamada de objeto. Sendo assim, ao 
#   criar uma Ferrari, estamos criando um objeto do tipo Carro e definindo seus atributos (cor, quantidade de portas, tipo de combustível, etc).



