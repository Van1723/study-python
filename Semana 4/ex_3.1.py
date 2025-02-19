# Exercício 3.1
# Implemente um programa que solicita a temperatura atual em graus Fahrenheit
# do usuário e exibe a temperatura em graus Celsius usando a fórmula:

# celsius=59( fahrenheit - 32 ).

# Seu programa deverá ser executado da seguinte forma:

# >>>
# Digite a temperatura em graus Fahrenheit: 50
# A temperatura em graus Celsius é 10.0

import math

temperaturaFahrenheit = float(input("Insira a temperatura em Fahrenheit")) ## captura os dados
celsius = (5/9) * (temperaturaFahrenheit - 32) ## calcula
celsius_ajustado = math.trunc(celsius * 10) / 10 ## tira numeros depois da virgula a mais
print("A temperatura em graus Celsius é ", celsius_ajustado) ## imprime o resultado




