# Dada uma lista com os nomes de 5 pessoas, liste um conjunto de tuplas de todas as
# combinações com 2 pessoas diferentes


if __name__ == '__main__':
    listName = ['fulano', 'fulano2', 'fulano3', 'fulnano4', 'fulano5']
    listComb = [(i, j) for i in listName for j in listName if i != j]
    print(len(listComb))
