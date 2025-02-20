# Exercício 3.14
# Implemente a função trocaPU(), que aceita uma lista como entrada e troca 
# o primeiro e último elementos da lista. Você pode considerar que a lista 
# não estará vazia. A função não deverá retornar nada.

# >>> ingredientes = [’farinha’, ’açúcar’, ’manteiga’, ’maçãs’]
# >>> trocaPU(ingredientes)
# >>> ingredientes
# [’maçãs’, ’açúcar’, ’manteiga’, ’farinha’]

def trocaPU(ingredientes):
    ingredientes.reverse()  # Inverte a lista original
    print(ingredientes)  # Exibe a lista invertida

minha_lista = ['farinha', 'açúcar', 'manteiga', 'maçãs']
trocaPU(minha_lista)

