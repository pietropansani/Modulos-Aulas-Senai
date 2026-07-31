# AULA COMPLETA: NUMEROS EM PYTHON

"""
O que vamos aprender:
1 - Tipos numericos
2 - Conversões de tipos
3 - Hierarquia númerica
4 - Operações matematicas
5 - Coerção de tipos
6 - Verificação de tipos
7 - Entrada de Dados
"""

print("==== TIPOS NÚMERICOS ====")

# EXEMPLO 01 - NUMERO INTEIRO

# criamos uma variavel chamada numero_inteiro
numero_inteiro = 10
# mostrar o valor
print("Valor:", numero_inteiro)
#Type() mostra qual é o tipo da variável
print("Tipo:", type(numero_inteiro))
# divisor
print("--------------------------------")

# EXEMPLO 02 - NUMERO DECIMAL
# Float é um numero com ponto decimal
numero_decimal = 3.14

print("Valor:", numero_decimal)
print("Tipo:", type(numero_decimal))

print("---------------------------------")

# EXEMPLO 03 - NUMERO COMPLEXO
# Um numero complex possui duas partes:
# Parte Real ( Numero Real )
# Parte Imaginaria ( multiplicada por j )

# Estrutura Geral:
# numero = a + bj

# a = partel real
# b = parte imaginária
# b = parte imaginária

numero_complexo = 2 + 3j

print("Valor:", numero_complexo)
print("Tipo:", type(numero_complexo))

print("-------------------------------")