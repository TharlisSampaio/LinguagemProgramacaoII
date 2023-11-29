class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def __str__(self) -> str:
        return f'{self.nome} {self.sobrenome}'
