import os

os.system("cls || clear")

class Aluno:
    # nome, idade
    #construtor
    def __init__(self, nome, idade) -> None:
        # atributos
        self.nome = nome
        self.idade = idade

# instanciar classe
aluno = Aluno("Marta", 22)

print(f"Nome: {aluno.nome}")
print(f"Idade: {aluno.idade}")