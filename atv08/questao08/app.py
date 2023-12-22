from carro import Carro
from aeronave import Aeronava
from moto import Moto

car1 = Carro('Duster', '2020')
air1 = Aeronava('Jatinho', 'Comercial')
moto1 = Moto('Fazer', 'esportiva')

print(car1.abastercer())
print(air1.abastercer())
print(moto1.abastercer())
