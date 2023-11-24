from conta import Conta


# Instanciar um objeto da classe Conta
c1 = Conta(1, 'Texugo', 1000, 500)
print(type(c1))  # Tipo de objeto
print(c1.titular)
print(c1.saldo)

# c1.saldo = 1500 # manipulando o atributo da classe Conta
print(c1.saldo)

# Não é recomendado pois altera a "receita" origianal (a class Conta)
# c1.chave_pix = 'tharlis.sampaio@com'
# print(c1.chave_pix)

c2 = Conta(2, 'Tharlis', 2000, 750)
# print(c2.chave_pix)

print(c2.saldo)
c2.sacar(500)
print(c2.saldo)
