arquivo = open('C:/Users/Tharlis Seixas/OneDrive/Documents/Git/LP2/manipulando_arquivos/exemplo01.txt')
linha = arquivo.readline()
# linha2 = arquivo.readline()
# print(linha)
# print(linha2)

while (linha != ''):
    print(linha)
    linha = arquivo.readline()

# for i in arquivo:
#     print('Outra forma de percorrer {i}')

arquivo.close()
