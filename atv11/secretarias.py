from funcionario import Funcionario, abstractmethod
from abc import ABC


class Secretaria(Funcionario, ABC):
    def __init__(self, nome, cpf, email, telefone, cargo, salario):
        super().__init__(nome, cpf, email, telefone, cargo, salario)

    @abstractmethod
    def calcular_bonificacao(self):
        pass

    def __str__(self) -> str:
        pass
