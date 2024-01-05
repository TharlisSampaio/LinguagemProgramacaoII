# __dict__ e vars

class Pessoa:
    ano_atual = 2024  # atributo de classe, poder ser acessado com self (mas não é recomendado)

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


p1 = Pessoa('João', 35)
print(p1.__dict__)  # irá mostrar um dicionario que mantem os valores da instância
print(vars(p1))

# ter cuidado, já que não é só leitura
p1.__dict__['outra'] = 'coisa'
print(vars(p1))
