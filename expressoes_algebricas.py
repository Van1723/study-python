# Escreva expressões algébricas Python correspondentes aos seguintes comandos:  
  
# A soma dos 5 primeiros inteiros positivos.
# A idade média de Sara (idade 23), Mark (idade 19) e
# Fátima (idade 31).
# O número de vezes que 73 cabe em 403.
# O resto de quando 403 é dividido por 73.
# 2 à 10ª potência.
# O valor absoluto da distância entre a altura de Sara
# (54 polegadas) e a altura de Mark (57 polegadas).
# O menor preço entre os seguintes preços: R$ 34,99,
# R$ 29,95 e R$ 31,50.

## soma
Soma = 1 +2 + 3 + 4 + 5
print(Soma)

#A idade média de Sara (idade 23), Mark (idade 19) e
# Fátima (idade 31).

Media = (23 + 19 + 31) // 3
print(Media)


# O número de vezes que 73 cabe em 403.

multiplicacao = 403 / 73
print(multiplicacao)

##O resto de quando 403 é dividido por 73.
resto = 403 % 73
print(resto)

#2 à 10ª potência.

potencia = 2^10 
print(potencia)


##O valor absoluto da distância entre a altura de Sara
# (54 polegadas) e a altura de Mark (57 polegadas).
distancia = 57 - 54
print(distancia)

#O menor preço entre os seguintes preços: R$ 34,99,
# R$ 29,95 e R$ 31,50.

Precos = [34.99,29.95,31.50] ## array construido
menor = min(Precos) ## cria variavel do menor
print(menor) ## saida de dados