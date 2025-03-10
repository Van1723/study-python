
# Implemente a função meuIMC(), que aceita como entrada a altura de uma pessoa
# (em metros) e o peso (em quilos) e calcula o Índice de Massa Corporal (IMC)
# dessa pessoa. A fórmula do IMC é:

# imc=pesoaltura2.

# Sua função deverá exibir a string 'Abaixo do peso' se o imc < 18.5,
# 'Normal' se 18,5 <= imc < 25, e
# 'Sobrepeso' se imc >= 25.
  
# >>> meuIMC(86, 1.90)
# Normal
# >>> meuIMC(63, 1.90)
# Abaixo do peso



altura = float(input("Insira sua altura em metros: "))
peso = float(input("Insira seu peso em kg: "))

def meuIMC(altura, peso): 
    imc = peso / (altura ** 2)

    if imc < 18.5:  
        print(f"Seu IMC é: {round(imc, 2)} - Abaixo do peso")
    elif 18.5 <= imc < 25:
        print(f"Seu IMC é: {round(imc, 2)} - Normal")
    elif 25 <= imc < 30:
        print(f"Seu IMC é: {round(imc, 2)} - Sobrepeso")
meuIMC(altura, peso)

