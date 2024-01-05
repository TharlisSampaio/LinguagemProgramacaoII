# Métodos de classe + factories (fábricas)
# São métodos onde 'self' será 'cls', ou seja
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe

# classmethod é um decorador em Python que é usado para definir um método de classe.
# Um método de classe é um método que é vinculado à classe em vez de suas instâncias.
# Isso significa que o método pode ser chamado tanto na própria classe quanto em qualquer uma de suas instâncias.

class Pessoa:
    ano = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('Hey')

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)


# print(Pessoa.ano)
p1 = Pessoa('João', 34)
p2 = Pessoa.criar_com_50_anos('Helena')
print(vars(p2))
