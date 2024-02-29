arquivo = open('C:/Users/Tharlis Seixas/OneDrive/Documents/Git/LP2/manipulando_arquivos/exemplo01.txt', 'w')

for i in range(1, 11):
    arquivo.write(f'Valor: {i}\n')

arquivo.close()
