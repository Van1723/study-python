# Traduza os comandos a seguir para expressões Booleanas em Python e avalie-as:

# A soma de 2 e 2 é menor que 4.
# O valor de 7 // 3 é igual a 1 + 1.
# A soma de 3 ao quadrado e 4 ao quadrado é igual a 25.
# A soma de 2, 4 e 6 é maior que 12.
# 1387 é divisível por 19.
# 31 é par. (Dica: o que o resto lhe diz quando você
# divide por 2?)
# O preço mais baixo dentre R$ 34,99, R$ 29,95 e R$ 31,50
# é menor que R$ 30,00.*


x = 2 ## cria var
y = 2 # cria var
soma = x + y # cria var soma

if soma < 4: ## teste de seleção
 print("sim verdadeiro") ## saida de dados
else:  ## teste de seleção
  print("a soma não é menor que 4") ## saida de dados


# O valor de 7 // 3 é igual a 1 + 1.

a = 7
b = 3

divisaoInteira = 7 // 3

if divisaoInteira == 1 + 1:
  print("sim verdadeiro")
else:
  print("Não é verdadeiro")
  

# A soma de 3 ao quadrado e 4 ao quadrado é igual a 25.

soma1 = 3^2
soma2 = 4^2
somaTotal = soma1 + soma2

if somaTotal == 25:
  print("sim é verdadeiro")
else:
  print("Não é verdadeiro")



# A soma de 2, 4 e 6 é maior que 12.

calculo = 2 + 4 + 6
if calculo > 12:
   print("sim é verdadeiro")
else:
  print("Não é verdadeiro")


# 1387 é divisível por 19.

divisao = 1387 / 19
if divisao == 73:
 print("sim é verdadeiro")
else:
  print("Não é verdadeiro")


# 31 é par. (Dica: o que o resto lhe diz quando você
# divide por 2?)

par = 31 % 2
if par == 0:
  print(" é par")
else:
  print("não é par")


# O preço mais baixo dentre R$ 34,99, R$ 29,95 e R$ 31,50
# é menor que R$ 30,00.*
Precos = [34.99, 29.95, 31.50]
menorPreco = min(Precos)  # Encontra o menor preço
menorQue30 = menorPreco < 30.00  # Verifica se é menor que 30

if menorQue30:
    print("O menor preço é", menorPreco)
else:
    print("Nenhum preço é menor que R$ 30,00.")
