# Exercício 3.9
# Implemente a função perímetro(), que aceita, como entrada, o raio de um 
# círculo (um número não negativo) e retorna o perímetro do círculo. Você deverá 
# escrever sua implementação em um módulo chamado perímetro.py. 
# Um exemplo de uso é:

# >>> perimeter(1)
# 6.283185307179586

import math

def perimetro(raio):
    if raio < 0:
        raise ValueError("O raio não pode ser negativo.")
    return 2 * math.pi * raio
print(perimetro(1)) 

 