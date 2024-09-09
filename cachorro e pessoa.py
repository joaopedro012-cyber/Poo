# Definição da classe Pessoa
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar_informacoes(self):
        print(f"Nome: {self.nome}, Idade: {self.idade} anos")

# Criação de objetos da classe Pessoa
pessoa1 = Pessoa("João", 23)
pessoa2 = Pessoa("Joana", 50)

# Mostrar informações das pessoas
pessoa1.mostrar_informacoes()
pessoa2.mostrar_informacoes()


# Definição da classe Cao
class Cao:
    def __init__(self, raca, idade):
        self.raca = raca
        self.idade = idade

    def mostrar_informacoes(self):
        print(f"Raça: {self.raca}, Idade: {self.idade} anos")

# Criação de objetos da classe Cao
cao1 = Cao("Shitzu", 4)
cao2 = Cao("Pit Bull", 1)

# Mostrar informações dos cães
cao1.mostrar_informacoes()
cao2.mostrar_informacoes()

