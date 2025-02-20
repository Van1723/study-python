# Exercício 3.12
# Desenhe um diagrama representando o estado dos nomes e objetos após 
# esta execução:

# >>> a = [5, 6, 7]
# >>> b = a
# >>> a = 3


a = [5, 6, 7]
b = a
a = 3


# Antes da linha "a = 3":

#     a  --->  [5, 6, 7]  <---  b

# Depois da linha "a = 3":

#     a  --->  3
#     b  --->  [5, 6, 7]
