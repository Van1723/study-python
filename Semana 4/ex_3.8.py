# Exercício 3.8
# Defina, diretamente no shell interativo, a função média(), que aceita dois
# números como entrada e retorna a média dos números. Um exemplo de uso é:

# >>> average(2, 3.5)
# 2.75

def media():
    numeros = input("Digite os números separados por espaço: ").split() ##capta dados
    numeros = [float(num) for num in numeros]  # Converte para numero decimal
    return sum(numeros) / len(numeros) if numeros else 0  ## faz a média
resultado = media() ## resultado
print(f"Média: {resultado:.2f}") ## imprime o resultado  