# Atributos de classe

class Pessoa:
    ano_atual = 2024  # atributo de classe, poder ser acessado com self (mas não é recomendado)

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


p1 = Pessoa('João', 40)
p2 = Pessoa('Tadeu', 24)

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
