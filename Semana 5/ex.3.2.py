

# Traduza estas instruções condicionais em instruções if do Python:

  
# a.	Se idade é maior que 62, exiba 'Você pode obter benefícios de pensão'.
# b.	Se o nome está na lista ['Musial', 'Aaraon', 'Williams', 'Gehrig', 'Ruth'],
# exiba 'Um dos 5 maiores jogadores de beisebol de todos os tempos!'.
# c.	Se golpes é maior que 10 e defesas é 0, exiba 'Você está morto…'.
# d.	Se pelo menos uma das variáveis booleanas norte, sul, leste e oeste for True,
# exiba 'Posso escapar.'.

## a.	Se idade é maior que 62, exiba 'Você pode obter benefícios de pensão'
idade = int(input("digite sua idade"))  ## cria variavel
if (idade > 62 ): ## condição
  print("Você pode obter benefícios de pensão") ## imprime resultado
else: ## condição diferente da anterior
  print("você ainda não pode obter benefícios de pensão") ## imprime resultado





## b.	Se o nome está na lista ['Musial', 'Aaraon', 'Williams', 'Gehrig', 'Ruth'],
lista = ['Musial', 'Aaraon', 'Williams', 'Gehrig', 'Ruth']

if 'Musial' in lista: 
   print('Um dos 5 maiores jogadores de beisebol de todos os tempos!') 
else: 
   print('O nome não está cadastrado. ')


# c.	Se golpes é maior que 10 e defesas é 0, exiba 'Você está morto…'.


golpes = 11
defesas = 0
if (golpes >10 and defesas == 0):
   print('Você está morto…')


# d.	Se pelo menos uma das variáveis booleanas norte, sul, leste e oeste for True,
# exiba 'Posso escapar.'.

norte = True
sul = False
leste = False
oeste = False

direcoes = [norte, sul, leste, oeste]

if any(direcoes):
   print('Posso escapar.')

