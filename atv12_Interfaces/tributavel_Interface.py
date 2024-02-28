import abc


class TributavelInterface(abc.ABC):
    """
    A interface TributavelInterface define como irá calcular o imposto
    sobre um tributavel.
    """
    @abc.abstractmethod
    def valor_imposto(self):
        """
        Método que deve ser implementado pelas subclasses.
        Retorna o valor do imposto (float).
        """
        pass


if __name__ == '__main__':
    help(TributavelInterface)
