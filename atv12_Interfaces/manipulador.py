from tributavel_Interface import TributavelInterface


class ManipuladorDeTributaveis:
    def calcular_impostos(self, lista_tributaveis):
        total_de_tributos = 0
        for obj in lista_tributaveis:
            if (isinstance(obj, TributavelInterface)):
                total_de_tributos += obj.valor_imposto()
            else:
                print(f'O objetos da classe {obj.__class__.__name__} não é tributavel!\n'
                      f'Apenas os tributáveis serão somados ao total.')
        return total_de_tributos

        # try:
        # if (isinstance(obj, TributavelInterface)):
        #     print('É tributavel')
        # else:
        #      print('Não é tributavel')
        # except AttributeError:
        #     print(f'{obj.__class__.__name__} Não é tributavel!')
