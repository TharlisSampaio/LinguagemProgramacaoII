from abc import ABC, abstractmethod


class Funcionario(ABC):
    def __init__(self, nome, cpf, email, telefone, cargo, salario):
        self._nome = nome
        self._cpf = cpf
        self._email = email
        self._telefone = telefone
        self._cargo = cargo
        self._salario = salario

    @abstractmethod
    def calcular_bonificacao(self, porcentagem, adicional):
        pass

    @property
    def get_nome(self):
        return self._nome

    @get_nome.setter
    def set_nome(self, nome):
        self._nome = nome

    @property
    def get_cpf(self):
        return self._cpf

    @get_cpf.setter
    def set_cpf(self, cpf):
        self._cpf = cpf

    @property
    def get_email(self):
        return self._email

    @get_email.setter
    def set_email(self, email):
        self._email = email

    @property
    def get_telefone(self):
        return self._telefone

    @get_telefone.setter
    def set_telefone(self, telefone):
        self._telefone = telefone

    @property
    def get_cargo(self):
        return self._cargo

    @get_cargo.setter
    def set_cargo(self, cargo):
        self._cargo = cargo

    @property
    def get_salario(self):
        return self._salario

    @get_salario.setter
    def set_salario(self, salario):
        self._salario = salario

    def __str__(self) -> str:
        return f'Nome: {self.get_nome}, Email: {self.get_email}, Cargo: {self.get_cargo}, Salario: {self.get_salario}'
