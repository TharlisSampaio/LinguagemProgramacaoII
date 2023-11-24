# Escreva uma função onde o usuário pode informar vários dados pessoais (Nome, Sobrenome, CPF e
# idade). E imprima somente seu nome e sua idade, caso sejam informados. Se ele não passar nada, não
# imprima nada. Entrada: Nome='Júnior', Sobrenome='Limeira', Idade=29, Profissao='Professor' Saída:
# Nome: Júnior Idade: 29

def dadosPessoal(name='', sobrenome='', cpf='', idade=0):
    if name != '' and idade == 0:
        print(f'Nome: {name}')

    if name != '' and idade != 0:
        print(f'Name: {name}, Idade: {idade}')
    # print(name, sobrenome, cpf, idade)


if __name__ == '__main__':
    dadosPessoal('Tharlis', idade=19)
