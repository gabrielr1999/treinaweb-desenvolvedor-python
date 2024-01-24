from usuario import Usuario

usuario = Usuario("João", 10, "Silva")

for x in range(1, 10):
    print(f"Olá, {usuario.nome} {usuario.sobrenome}, sua idade é {usuario.idade}")

    if x ==2:
        continue
    if x == 8:
        break

    print(x)

    if usuario.idade >= 18:
        print(f"{usuario.nome} é maior de idade")
    else:
        print(f"{usuario.nome} é menor de idade")
else: 
    print("O loop entrou no else")

idade2 = 1
while idade2!= 0:
    nome2 = input("Digite seu nome: ")
    idade2 = int(input("Digite sua idade: "))
    sobrenome2 = input("Digite seu sobrenome: ")

    usuario2 = Usuario(nome2, idade2, sobrenome2)

    if usuario2.idade == 99:
        break
    if usuario2.idade == 98:
        continue

    print(f"Olá, {usuario2.nome} {usuario2.sobrenome}, sua idade é {usuario2.idade}")

    media_idades = (usuario.idade + usuario2.idade) / 2
    print(f"A média das idades é: {media_idades}")

    if usuario2.idade <= 17:
        print(f"{usuario2.nome} é adolecente")
    elif usuario2.idade >= 18 and usuario2.idade <= 50:
        print(f"{usuario2.nome} é adulto")
    else:
        print(f"{usuario2.nome} é idoso") 
else:
    print("o loop entrou no else")