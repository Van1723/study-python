# Exercício 3.10
# Escreva a função negativos(), que aceita uma lista como entrada e exibe, um por
# linha, os valores negativos na lista. A função não deverá retornar nada.

# >>> negatives([4, 0, −1, −3, 6, −9])
# -1
# -3
# -9
lista = [4, 0, -1, -3, 6, -9]  ## cria variável em lista
def negativos(lista):  ## cria função
    for num in lista:    ## cria variavel num que é cada elemento de lista
        if num < 0:     ## se for menor que zero
            print(num)    ## exibe os numeros que atenderam a condição no console
negativos([4, 0, -1, -3, 6, -9]) ## mostra todos no console