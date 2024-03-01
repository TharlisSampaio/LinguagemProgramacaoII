PATH = 'C:/Users/Tharlis Seixas/OneDrive/Documents/Git/LP2/atv13/results/'


class IsEqualArquivos:
    def __init__(self, primeiro_arquivo, segundo_arquivo):
        self._primeiro_arquivo = primeiro_arquivo
        self._segundo_arquivo = segundo_arquivo

    def is_equal(self):
        try:
            with open(f'{PATH}{self._primeiro_arquivo}.txt', 'r') as arg:
                with open(f'{PATH}{self._segundo_arquivo}.txt', 'r') as arg2:
                    arg = arg.read()
                    arg2 = arg2.read()
                    return arg in arg2
        except Exception as error:
            print(error)


if __name__ == '__main__':
    equal = IsEqualArquivos('compara_a', 'compara_b')
    print(equal.is_equal())
