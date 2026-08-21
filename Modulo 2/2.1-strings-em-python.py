# -----------------------------------------------
# 1) CRIAÇÃO DE STRINGS
# -----------------------------------------------

# Strings, são textos em python
# Podem ser criadass usando aspas simples ou duplas

texto1 ="Python"
texto2 = 'Curso de Python'
texto3 = "Copa'padrao fifa'"
texto4 = 'Copa "padrão fifa"'

print(texto1, texto2, texto3, texto4)

# Python permite misturar aspas simples e duplas, dentro das strings sem precisar escapar caracteres

# -----------------------------------------------
# 2) STRINGS MULTILINHA
# -----------------------------------------------

# Usando três aspas (""" ou ''') para criar textos que ocupam várias linhas.

menu = """\
Uso: programa [OPÇÕES]
-h Exibe Ajuda
-U Url do Dataset
"""
print(menu)

# Esse formato é muito usado para:
# - Menus
# - documentação
# - textos longos

# -----------------------------------------------
# 3) CONCATENAÇÃO AUTOMÁTICA
# -----------------------------------------------
# Quando duas strings aparecem lado a lado, o Python junta automaticamente

texto = ("Copa " "2026 " "Neymar é show mesmo?")
print(texto)

# -----------------------------------------------
# 4) STRINGS COMO SEQUÊNCIAS
# -----------------------------------------------
# Uma string funciona como uma sequência de caracteres, cada caractere possui um indice

st = "maracana"
print("Primeira Letra:", st[0])
# só exibir a letra: m

print("ultima letra: ", st[-1])

print("Trecho 1:4:", st[1:4])

print("Do ínicio até 3:", st[:3])

print("Do 2 até o fim:", st[2:])

print("Tamanho", len(st))

# -----------------------------------------------
# 5) OPERAÇÕES CPOM STRINGS
# -----------------------------------------------
# Python permite vvárias operações com strings

print("m" in st)
# Signifca que "m" existe dentro da variável st

print("x" not in st)
# Significa que "X" não existe na string

print("m" * 10)
# Multiplicação de uma String

print("m" + "aracana" + texto1)
# Operador + concatena strings

# -----------------------------------------------
# 6) STRINGS SÃO IMUTÁVEIS
# -----------------------------------------------
# Strings não podem ser aalteradas diretamente!!!
# isso significa que o conteudo original não muda
# O que acontece é a criação de uma nova string.

texto5 = "python 3"

texto5 = texto5.replace("3", "2")

print(texto5)

# -----------------------------------------------
# 7) STRINGS COMO SEQUÊNCIAS
# -----------------------------------------------
# Strings possuem vários metodos uteis.

cidade = "maracana"
# Coloca a primeira letra em maiúscula.
print(cidade.capitalize())

# conta quantas vezes "a" aparece
print(cidade.count("a"))

# Verificar se começa com "m"
print(cidade.startswith("m"))

# Verificar se termina com "z"
print(cidade.endswith("m"))

frase = "copa de 2002"
print(frase.split(" "))

# -----------------------------------------------
# 8) FORMATAÇÃO DE STRINGS
# -----------------------------------------------