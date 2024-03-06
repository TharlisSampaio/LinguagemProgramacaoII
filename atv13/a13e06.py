PATH = 'C:/Users/Tharlis Seixas/OneDrive/Documents/Git/LP2/atv13/results/'


class MediaDeNotaDoAluno:
    def __init__(self, arq_alunos, arq_notas):
        self._arq_alunos = arq_alunos
        self._arq_notas = arq_notas

    def calcular_media_de_alunos(self, saida_arquivo):
        try:
            with open(f'{PATH}{self._arq_alunos}.txt', 'r') as arq1, open(f'{PATH}{self._arq_notas}.txt', 'r') as arq2:
                alunos = [i.strip() for i in arq1.readlines()]
                notas = [list(map(float, i.split())) for i in arq2]

            with open(f'{PATH}{saida_arquivo}.txt', 'w') as arq_saida:
                for i in range(len(alunos)):
                    aluno = alunos[i]
                    media = sum(notas[i])/notas[i].__len__()
                    arq_saida.write(f'Aluno: {aluno}, media: {media:.2f}\n')

        except Exception as error:
            print(error)


if __name__ == '__main__':
    mddna = MediaDeNotaDoAluno('alunos', 'notas')
    mddna.calcular_media_de_alunos('medias_alunos')
