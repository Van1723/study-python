# exercício 3.11
# Acrescente a docstring retorna a média de x e y à função média() e a docstring
# exibe os números negativos contidos na lista lst à função negativos() dos 
# Problemas Práticos 3.8 e 3.10. Verifique seu trabalho usando a ferramenta de 
# documentação help(). Você deverá receber, por exemplo:

# >>> help(média)
# Ajuda sobre a função média no módulo __main__:
# média(x, y)
#  retorna a média de x e y



def media():
    """"Exibe a media de x e y"""
    numeros = input("Digite os números separados por espaço: ").split() ##capta dados
    numeros = [float(num) for num in numeros]  # Converte para numero decimal
    return sum(numeros) / len(numeros) if numeros else 0  ## faz a média
resultado = media() ## resultado
print(f"Média: {resultado:.2f}") ## imprime o resultado 
print(help(media)) 



lista = [4, 0, -1, -3, 6, -9]  ## cria variável em lista
def negativos(lista):  ## cria função
 """Exibe os números negativos contidos na lista lst. """      
for num in lista:    ## cria variavel num que é cada elemento de lista
        if num < 0:     ## se for menor que zero
            print(num)    ## exibe os numeros que atenderam a condição no console
        negativos([4, 0, -1, -3, 6, -9]) ## mostra todos no console
print(help(negativos)) 
        



