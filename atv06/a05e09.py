# Crie uma função anônima que converta uma lista de temperaturas em Celsius para Fahrenheit. Você
# deve criar sua função lambda, dentro de uma função map() e imprimir as temperaturas com duas casas
# decimais. Fahrenheit = 9/5 * Celsius + 32

if __name__ == '__main__':
    temp_celcius = [32, 22, 38, 12]
    result = map(lambda x: 9/5*x+32, temp_celcius)
    print(list(result))
