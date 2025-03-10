# Traduza estas declarações em instruções if/else do Python:

# a.	Se ano é divisível por 4, exiba 'Pode ser um ano bissexto.'; caso contrário,
# exiba 'Definitivamente não é um ano bissexto.'
# b.	Se a lista bilhete é igual à lista loteria, exiba 'Você ganhou!'; se não, exiba
# 'Melhor sorte da próxima vez…'.

ano = int(input("Digite o ano"))
if(ano // 4):
    print('Pode ser um ano bissexto.')
else:
    print('Definitivamente não é um ano bissexto.')



# b.	Se a lista bilhete é igual à lista loteria, exiba 'Você ganhou!'; se não, exiba
# 'Melhor sorte da próxima vez…'.
listaLoteria = [2,5,25,35,60]
bilhete1 = [2,20,30,50,55]
bilhete2 = [2,5,25,35,60]

if(bilhete1 == listaLoteria):
    print('Você ganhou!')
else:
    print('Melhor sorte da próxima vez…')



if(bilhete2 == listaLoteria):
    print('Você ganhou!')
else:
    print('Melhor sorte da próxima vez…')

