import string
PATH = 'C:/Users/Tharlis Seixas/OneDrive/Documents/Git/LP2/atv13/results/'


class AnaliseDeArquivo:
    def __init__(self):
        pass

    def analisar_arquivo(self, arquivo):
        vogais = ['a', 'e', 'i', 'o', 'u']
        try:
            with open(f'{PATH}{arquivo}.txt', 'r') as arq:
                conteudo = arq.read()

                total_caracteres = conteudo.__len__()
                total_vogais = len([i for i in conteudo if i.lower() in vogais])
                total_consoante = len([i for i in conteudo if i.lower() not in vogais])
                total_carac_especial = len([i for i in conteudo if i.lower() in string.punctuation])
                total_palavras = len(conteudo.split())
                total_linhas = conteudo.count('\n')

            with open(f'{PATH}saida_da_analise_dos_arquivos.txt', 'a') as arq_out:
                arq_out.write(f'Nome do arquivo: {arquivo}\n')
                arq_out.write(f'Total de caracteres: {total_caracteres}\n')
                arq_out.write(f'Total de vogais: {total_vogais}\n')
                arq_out.write(f'Total de consoantes: {total_consoante}\n')
                arq_out.write(f'Total de caracteres especiais: {total_carac_especial}\n')
                arq_out.write(f'Total de palavras: {total_palavras}\n')
                arq_out.write(f'Total de linhas: {total_linhas}\n')

        except FileNotFoundError as erro:
            print(erro)


if __name__ == '__main__':
    anl = AnaliseDeArquivo()
    anl.analisar_arquivo('compara_a')
