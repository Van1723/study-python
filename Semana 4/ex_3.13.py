# Exercício 3.13
# Suponha que uma lista não vazia time foi atribuída. Escreva uma instrução 
# Python ou instruções que mapeiam o primeiro e último valor da lista. Assim, se 
# a lista original for:

# >>> time = [’Ava’, ’Eleanor’, ’Clare’, ’Sarah’]
  
# então a lista resultante deverá ser:
  
# >>> time
# [’Sarah’, ’Eleanor’, ’Clare’, ’Ava’]

time = ['Ava', 'Eleanor', 'Clare', 'Sarah']
time.reverse()  # Inverte a lista original

print(time)  # Exibe a lista invertida
print(time[0])  # Exibe o primeiro elemento da lista invertida
print(time[-1])  # Exibe o último elemento da lista invertida