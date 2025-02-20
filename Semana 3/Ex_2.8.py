# Em que ordem os operadores nas expressões a seguir são avaliados?

    
# a.	2 + 3 == 4 or a >= 5 : Ordem de avaliação:

# 2 + 3 → 5
# 5 == 4 → False
# a >= 5 (depende do valor de a)
# False or (a >= 5) → resultado final depende de a
# b.	lst[1] * -3 < -10 == 0

# lst[1] * -3 → Multiplicação primeiro
# lst[1] * -3 < -10 → Comparação
# -10 == 0 → Comparação
# (lst[1] * -3 < -10) == 0 → Comparação final
# c.	(lst[1] * -3 < -10) in [0, True]
# st[1] * -3 → Multiplicação
# lst[1] * -3 < -10 → Comparação
# (< resultado anterior >) in [0, True] → Verifica se está na lista
# d.	2 * 3**2
# 3**2 → Exponenciação primeiro (** tem maior precedência)
# 2 * 9 → Multiplicação
# e.	4 / 2 in [1, 2, 3]
# 4 / 2 → Divisão
# 2 in [1, 2, 3] → Verificação de pertencimento
