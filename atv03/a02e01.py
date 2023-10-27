# Listar os números de 1 a 10^7
# que são divisíveis por 7

if __name__ == '__main__':
    print('Digite um numero inteiro n para a potenciação 10^n: ')
    n = int(input())
    listResult = [i for i in range(10**n) if i % 7 == 0]
    print(listResult)
