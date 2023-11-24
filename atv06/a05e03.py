# Desenvolva uma função que aceite qualquer quantidade e tipo de argumentos posicionais (*args) e
# palavras-chave com valores (**kwargs) para imprimir os argumentos posicionais na ordem inversa de
# entrada e as palavras-chave com seus valores em ordem alfabética.

def func(*args, **kwargs):
    listaPosicional = [i for i in args]
    print(listaPosicional, kwargs)


if __name__ == '__main__':
    func(1, 3, 2, 6, 4, name='Tharlis', sobrenome='Sampaio', idade=24)
