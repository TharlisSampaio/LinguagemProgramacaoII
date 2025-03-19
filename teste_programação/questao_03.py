# 3. Funções (Intermediário): Crie uma função chamada fatorial que receba um número
# inteiro como parâmetro e retorne o fatorial desse número.
# Utilize recursão para implementar a função.

def fatorial(n):
    if n == 1 or n == 0:
        return 1

    return n * fatorial(n - 1)


if __name__ == '__main__':
    print(fatorial(5))
