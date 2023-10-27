# Dado um dicionário qualquer, obtenha outro dicionário onde as chaves serão os
# valores e vice-versa.

if __name__ == '__main__':
    dicioNamaSobren = {'tharlis': 'Sampaio', 'Manoel': 'Limeira'}
    dicioResult = {dicioNamaSobren[f'{i}']: i for i in dicioNamaSobren}
    print(dicioResult)
