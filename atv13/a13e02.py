PATH = 'C:/Users/Tharlis Seixas/OneDrive/Documents/Git/LP2/atv13/results/'


class OrdenarInteiros:
    def __init__(self, entrada, saida):
        self._entrada = entrada
        self._saida = saida
        self._vogais = ['a', 'e', 'i', 'o', 'u']

    def ordena_inteiros(self):
        try:
            with open(f'{PATH}{self._entrada}.txt', 'r') as arg:
                with open(f'{PATH}{self._saida}.txt', 'w') as arg2:
                    lista = arg.read().split(' ')
                    interios_ordenados = sorted([int(x) for x in lista])
                    for i in interios_ordenados:
                        arg2.write(f'{i} ')
        except Exception as error:
            print(error)


if __name__ == '__main__':
    ordn = OrdenarInteiros('inteiros_desordenado', 'inteiros_ordenados')
    ordn.ordena_inteiros()
