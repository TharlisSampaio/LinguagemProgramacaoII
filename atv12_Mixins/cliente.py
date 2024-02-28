class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self._nome = nome
        self._sobrenome = sobrenome
        self._cpf = cpf

    def __str__(self):
        return f'{self._nome} {self._sobrenome}'
