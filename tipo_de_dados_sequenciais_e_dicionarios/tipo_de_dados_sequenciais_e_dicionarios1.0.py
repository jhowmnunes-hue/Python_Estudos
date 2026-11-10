# Criando uma lista com alguns elementos
lista = [10, 20, 30, 40, 50]

# Acessando elementos individuais da lista
primeiro_elemento = lista[0]
segundo_elemento = lista[1]

# Imprimindo os elementos acessados
print(f"O primeiro elemento da lista é {primeiro_elemento}")
print(f"O segundo elemento da lista é {segundo_elemento}")

#adicionando um elemento ao final da lista
lista.append(60)
print(f"Lista após adicionar 60: {lista}")

# Inserindo um elemento em uma posição especifica
lista.insert(2, 25) #Inserindo 25 na posição 2

# Removendo um elemento da lista
lista.remove(40) #remove o primeiro valor 40 encontrado
print(f"Lista após remover 40: {lista}")

# Removendo o último elemento da lista
ultimo_elemento = lista.pop()
print(f"Elemento removido: {ultimo_elemento}")
print(f"Lista após remover o ultimo elemento: {lista}")

# Acessando um subgrupo da lista (fatiamento)
sub_lista = lista[1:4]
print(f"Sub-lista (elementos de índice 1 a 3): {sub_lista}")

# Ordenando a lista
lista.sort()
print(f"Lista ordenada: {lista}")

# Iterando sobre os elementos da lista
print("Iterando sobre a lista:")
for elemento in lista:
    print(elemento)
