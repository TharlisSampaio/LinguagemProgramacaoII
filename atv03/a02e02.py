# Listar todos os números de 1 a 10^7
# que tenham o digito 7


if __name__ == '__main__':
    n = int(input())
    listResult = [print(i) for i in range(10**n) if f'{i}'.__contains__('7')]
    print(listResult)
