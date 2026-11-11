# Criando uma string
texto = 'Olá, mundo!'

# Acessando caracteres individuais
primeiro_caractere = texto[0] #lendo o primeiro
ultimo_caractere = texto[-1] #lendo de tras para frente (por ser negativo)

print(f"Primeiro caractere: {primeiro_caractere}")
print(f"ultimo caractere: {ultimo_caractere}")

# Fatiando uma string
sub_texto = texto [5:10]
print(f'Substring (indices 5 a 9): {sub_texto}')

# Concatenando strings
saudacao = "Olá"
nome = "Alice"
frase = saudacao + "," + nome + "!"
print(f"Frase concatenada: {frase}")

# Dividindo uma string em uma lista
lista_palavras = texto.split() #funcao split = pega palavra da string e separa, sabe que a palavra terminou pelo espaçõ em branco ex: se tiver ponto exclamacao junto a palavra ele entende que a palavra nao acabou
print(f"Lista de palavras: {lista_palavras}")

# Substituindo partes de uma string
texto_modificado = texto.replace("Mundo", "Python")
print(f"Texto modificado: {texto_modificado}")

# Convertendo para maúsculas e minúsculas
texto_maiusculo = texto.upper()
texto_minusculo = texto.lower()
print(f"Texto em maiúsculas: {texto_maiusculo}")
print(f"Texto em minúsculas: {texto_minusculo}")

# Removendoespaços em branco (trim)
texto_espacos = " Olá, Mundo:  "
texto_sem_espacos = texto_espacos.strip() #removendo espaco que tem antes e depois, nao os do meio.
print(f"Texto sem espaços extras: {texto_sem_espacos}")

# Verificando a presença de substring
if "Mundo" in texto:
    print('A palavra "Mundo" está presente no texto.')

# Formatação de string
idade = 30
cidade = "São Paulo"
frase_formatada = f'Meu nome é {nome}, tenho {idade} anos e moro em {cidade}.'
print(f"Frase formatada: {frase_formatada}")

# Outro método de formatação
frase_formatada_2 = "Meu nome é {}, tenho {} anos e moro em {}.".format(nome, idade, cidade)
print(f"Outra frase formatada: {frase_formatada_2}")

