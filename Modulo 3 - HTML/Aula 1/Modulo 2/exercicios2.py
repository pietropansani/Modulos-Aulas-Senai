# ======================================================
# MÓDULO 1 — CRIAÇÃO DE STRINGS
# ======================================================

# EX1
# Crie uma variável chamada texto1 com o valor "Logica"
# usando aspas duplas e exiba o conteúdo.

print("------------------------------------------------")
texto1 = "Logica"
print(texto1)
print("------------------------------------------------")

# EX2
# Crie uma variável chamada texto2 com o valor
# 'Eu sou top em python' usando aspas simples e exiba.

texto2 = 'Eu sou top em python'
print(texto2)
print("------------------------------------------------")

# EX3
# Crie uma string usando aspas simples que contenha
# aspas duplas dentro do texto: copa "padrão fifa".

string = 'copa "padrão fifa"'
print(string)
print("------------------------------------------------")

# EX4
# Crie uma string usando aspas duplas que contenha
# aspas simples dentro do texto: copa 'padrão fifa'.

string2 = "copa 'padrão fifa'"
print(string2)
print("------------------------------------------------")

# ======================================================
# MÓDULO 2 — STRINGS MULTILINHA
# ======================================================

# EX5
# Crie uma string multilinha representando um menu
# com as opções:
# -A  Exibe ajuda
# -E  Execute agora, quero jogar!

string_multilinha = """\
-A  Exibe ajuda
-E  Execute agora, quero jogar!
"""

print(string_multilinha)
print("------------------------------------------------")

# EX6
# Crie uma string multilinha contendo um poema
# com três versos.

poema = """\
No silêncio da noite eu ouvi o mar,
Levando sonhos que não podem voltar,
E estrelas nasceram só para te lembrar.
"""

print(poema)
print("------------------------------------------------")

# ======================================================
# MÓDULO 3 — CONCATENAÇÃO AUTOMÁTICA
# ======================================================

# EX7
# Use concatenação automática de literais para unir
# as palavras "Volei" e "top!".

ex7 = "Volei" " top!"
print(ex7)
print("------------------------------------------------")

# EX8
# Concatene automaticamente as strings
# "Python", " é ", "demais" em uma única string.

ex8 = "Python" " é " "demais"
print(ex8)
print("------------------------------------------------")

# ======================================================
# MÓDULO 4 — STRINGS COMO SEQUÊNCIAS
# ======================================================

# EX9
# Atribua "software" a uma variável chamada st
# e mostre a primeira letra da string.

st = "software"

print("Primeira letra:", st[0])
print("------------------------------------------------")

# EX10
# Usando a mesma string "software",
# mostre a última letra.

print("Última letra:", st[7])
print("------------------------------------------------")

# EX11
# Mostre os caracteres do índice 1 até o índice 4
# (sem incluir o 4) da string "software".

print(st[1:4])
print("------------------------------------------------")

# EX12
# Mostre os caracteres do início até o índice 3
# da string "software".

print(st[:3])
print("------------------------------------------------")

# EX13
# Mostre os caracteres do índice 2 até o final
# da string "software".

print(st[2:])
print("------------------------------------------------")

# EX14
# Mostre o tamanho da string "software"
# usando a função len().

print(len(st))
print("------------------------------------------------")

# EX15
# Acesse o último caractere de "software"
# usando índice positivo (sem usar -1).

print(st[7])
print("------------------------------------------------")

# EX16
# Mostre os caracteres que estão nos índices pares
# da string "software".

print(st[::2])
print("------------------------------------------------")

# EX17
# Inverta a string "software".

print(st[::-1])
print("------------------------------------------------")