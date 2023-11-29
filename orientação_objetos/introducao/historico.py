class Historico:
    def __init__(self):
        self.transacoes = []
        
    def __str__(self):
        for i in self.transacoes:
            print(i)
    