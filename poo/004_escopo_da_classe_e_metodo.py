# Escopo da classe e de métodos da classe

class Animal:
    # Escopo da classe onde estão o métodos ou atributo de classe
    def __init__(self, nome):
        # Escopo do método
        self.nome = nome  # pode ser chamado por qualquer método da classe

        variavel = 'valor'  # do escopo do '__init__'
        print(variavel)

    def comendo(self, alimento):
        return f'{self.nome} está comendo {alimento }'
