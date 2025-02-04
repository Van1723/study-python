# 3.	Realizar a leitura dos valores de quatro notas escolares bimestrais de
# um aluno representadas pelas variáveis N1, N2, N3 e N4.
# Calcular a média aritmética (variável MD) desse aluno e apresentar a mensagem
# “Aluno Aprovado com média” se a média obtida for maior ou igual a 5;
# caso contrário, apresentar a mensagem “Aluno Reprovado com média”. Informar
# também, após a apresentação das mensagens, o valor da média obtida pelo aluno.





notas = []  # Criando uma lista vazia
n = 4  # Quantidade de notas

for i in range(n):
    valor = float(input(f"Digite a {i+1}ª nota: "))  # Convertendo entrada para float
    notas.append(valor)  # Adicionando à lista

soma = sum(notas)  # Somando as notas
MD = soma / len(notas)  # Calculando a média


if MD < 5: ## teste seletivo
  print("Aluno Reprovado com média:", MD) ## saida de dados
else:
  print("“Aluno Aprovado com média", MD ) ## saida de dados






