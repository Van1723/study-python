# Dada a lista de notas de trabalho de casa dos alunos

# >>> notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]

# escreva:

  
# a.	Uma expressão que avalia para o número de 7 notas.
# b.	Uma instrução que muda a última nota para 4.
# c.	Uma expressão que avalia para a nota mais alta.
# d.	Uma instrução que classifica as notas da lista.
# e.	Uma expressão que avalia para a média das notas.


# a.	Uma expressão que avalia para o número de 7 notas.

notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]
numero = 7  
quantidade = notas.count(numero)

print(f"O número {numero} aparece {quantidade} vezes.")


# b.	Uma instrução que muda a última nota para 4.

notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]
notas[-1] = 4 ## muda ultima nota
print(notas) ## imprime notas

# c.	Uma expressão que avalia para a nota mais alta.
notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]
maiorNota = max(notas) ##  imprime maior nota
print("A maior nota é: ",maiorNota) ## imprime maior nota

# d.	Uma instrução que classifica as notas da lista.
notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]
maiorNota = max(notas)
menorNota = min(notas)

if  min(notas):
    print("Esse aluno teve a menor nota ", menorNota)
else: max(notas)
print("Esse aluno teve a maior nota ", maiorNota)


# e.	Uma expressão que avalia para a média das notas.

notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]

soma = sum(notas)  # Somando as notas
Media = soma / len(notas)  # Calculando a média
print("A média das notas é : ",Media)



