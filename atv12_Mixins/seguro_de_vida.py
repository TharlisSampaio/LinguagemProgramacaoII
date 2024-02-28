from tributavel import TributavelMixIn


class SeguroDeVida(TributavelMixIn):
    def __init__(self, numero_apolice, valor_do_seguro, titular):
        self._numero_apolice = numero_apolice
        self._valor_do_seguro = valor_do_seguro
        self._titular = titular

    def valor_imposto(self):
        valor_do_imposto = (self._valor_do_seguro * 0.05) + 34
        return valor_do_imposto


if __name__ == '__main__':
    seg = SeguroDeVida('22589', 25000, 'Tharlis')
    print(seg.valor_imposto())
