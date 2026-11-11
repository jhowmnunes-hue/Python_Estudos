# Criando um dicionario com alguns pares chave-valor
# Diferença de dicionario para lista: dicionario trabalha com esquema chave-valor
dicionario = {
    "nome": "Alice",
    "idade": 25,
    "cidade": "São Paulo"
}

# Acessando e imprimindo valores individuais usando chaves
nome = dicionario["nome"] #nome apontado pela chave nome
idade = dicionario["idade"] #idade apontado para chave idade
cidade = dicionario["cidade"] # cidade apontado para chave cidade

print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Cidade: {cidade}")

# Adicionando um novo par chave-valor ao dicionario
dicionario["profissão"] = "Engenheira"
print(f"Dicionario após adicionar profissão: {dicionario}")

# Modificando o valor associado a uma chave existente
dicionario["idade"] = 26
print(f"Dicionario após modificar a idade: {dicionario}")

# Removendo um par chave-valor do dicionário
del dicionario["cidade"]
print(f"Dicionário após remover a cidade: {dicionario}")

# Acessando todas as chaves e valores do dicionário
chaves = dicionario.keys()
valores = dicionario.values()

print(f"chaves: {list(chaves)}") #[str]
print(f"valores: {list(valores)}") #[str|int}

# Iterando sobre os pares chave-valor do dicionario
print("Iterando sobre o dicionário:")
for chave, valor in dicionario.items(): #vai imprimindo chave e valor
    print(f"{chave}: {valor}") #faz com que chave valor apareça em uma linha (em loop)

# Verificando se uma chave existe no dicionário
if "nome" in dicionario:
    print(f"O nome do dicionario é: {dicionario["nome"]}")
else:
    print('A chave "nome" não está no dicionário')

# Usando o método get() para acessar valores de forma segura
profissao = dicionario.get("profissao", "Desconhecido")
print(f"Profissão: {profissao}")

# Limpando todos os valores do dicionário
dicionario.clear()
print(f"Dicionario após limpar todos os elementos: {dicionario}")