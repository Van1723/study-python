# Exercício 2.3

# Escreva instruções Python que correspondem às ações a seguir e execute-as:

 
# Atribua o valor inteiro 3 à variável a.

a = 3
# Atribua 4 à variável b.
b = 4
# Atribua à variável c o valor da expressão a * a + b * b.
c = a * a + b * b


# Exercício 2.4

# Comece executando as instruções de atribuição:

s1 = 'ant'
s2 = 'bat'
s3 = 'cod'

print(s1)
print(s2)
print(s3)
            
# Escreva expressões Python usando s1, s2 e s3 e os
# operadores + e * a fim de avaliar para:  

  
# 'ant bat cod'

print(s1,s2,s3)
# ant ant ant ant ant ant ant ant ant ant'
print (s1,s1,s1,s1,s1,s1,s1,s1,s1,s1,s1)
# 'ant bat bat cod cod cod'
print(s1,s2,s2,s3,s3,s3)
# 'ant bat ant bat ant bat ant bat ant bat ant bat ant bat'
print(s1,s2,s1,s2,s1,s2,s1,s2,s1,s2,s1,s2,s1,s2)
# 'batbatcod batbatcod batbatcod batbatcod batbatcod'
print(s2+s2+s3,s2+s2+s3,s2+s2+s3,s2+s2+s3,s2+s2+s3)


# Exercício 2.5

# Comece executando a atribuição:

s = '0123456789'

# Agora, escreva expressões usando a string s e o operador de
# indexação que é avaliado como:  

   
# '0'
# '1'
# '6'
# '8'
# '9'

print(s[0])  # '0'
print(s[1])  # '1'
print(s[6])  # '6'
print(s[8])  # '8'
print(s[9])  # '9'