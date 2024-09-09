# Definição da classe Cliente
class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar_informacoes(self):
        print("Nome:", self.nome, ", Idade:", self.idade)

# Criação de objetos da classe Cliente
cliente1 = Cliente("João", 25)
cliente2 = Cliente("Maria", 30)

# Mostrar informações dos clientes
cliente1.mostrar_informacoes()
cliente2.mostrar_informacoes()


# Definição da classe Curso
class Curso:
    def __init__(self, nome_curso, matriculas):
        self.nome_curso = nome_curso
        self.matriculas = matriculas

    def mostrar_informacoes(self):
        print("Curso:", self.nome_curso, ", Matrículas:", self.matriculas)

# Criação de objetos da classe Curso
curso1 = Curso("Ciências da Computação", 30)
curso2 = Curso("Medicina", 50)

# Mostrar informações dos cursos
curso1.mostrar_informacoes()
curso2.mostrar_informacoes()
