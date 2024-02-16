from secretarias import Secretaria


class Executiva(Secretaria):
    def __init__(self, nome, cpf, email, telefone, cargo, salario):
        super().__init__(nome, cpf, email, telefone, cargo, salario)
        self._salario_com_bonificacao = salario

    def calcular_bonificacao(self, porcentagem=0, adicional=0):
        self._salario_com_bonificacao = self._salario + (self._salario * (porcentagem / 100)) + adicional

    def get_salario_bonificacao(self):
        return self._salario_com_bonificacao

    def __str__(self) -> str:
        return f'Nome: {self.get_nome}, Email: {self.get_email}, Cargo: {self.get_cargo}, Salario: {self.get_salario}, Salario com bonificação: {self.get_salario_bonificacao()}'


if __name__ == '__main__':
    ex1 = Executiva('blabla', '30030030030', 'blabla@blabla.com', '2452452452', 'Executiva', 4500)
    ex1.calcular_bonificacao(10, 100)
    print(ex1.__str__())