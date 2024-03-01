PATH = 'C:/Users/Tharlis Seixas/OneDrive/Documents/Git/LP2/atv13/results/'


class SubstituirVogais:
    def __init__(self, entrada, saida):
        self._entrada = entrada
        self._saida = saida
        self._vogais = ['a', 'e', 'i', 'o', 'u']

    def trocar_vogais(self):
        try:
            with open(f'{PATH}{self._entrada}.txt', 'r') as arg:
                with open(f'{PATH}{self._saida}.txt', 'w') as arg2:
                    arg = arg.read()
                    for i in arg:
                        if i.lower() in self._vogais:
                            arg2.write('*')
                        else:
                            arg2.write(i)
        except Exception as error:
            print(error)


if __name__ == '__main__':
    tr = SubstituirVogais('vogais', 'vogais_trocada')
    tr.trocar_vogais()
