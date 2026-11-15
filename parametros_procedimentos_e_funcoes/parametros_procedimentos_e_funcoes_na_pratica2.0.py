def encontrar_maior_elemento_iterativo(lista):
    """
    Encontra o maior elemento em uma lista de números inteiros de forma não recursiva.

    Args:
        lista: A lista de números inteiros.

    Returns:
        O maior elemento da lista.
    """

    # Verifica se a lista possui 0 ou 1 elemento
    if len(lista) <= 1:
        # Caso base: se a lista tiver no máximo 1 elemento, ele próprio é o maior
        return lista[0]

    # Assume inicialmente que o primeiro elemento é o maior de todos
    maior_elemento = lista[0]

    # Percorre todos os elementos da lista a partir do segundo elemento (índice 1 até o final)
    for numero in lista[1:]:
        # Compara o número atual do loop com o maior elemento encontrado até o momento
        if numero > maior_elemento:
            # Se o número atual for maior, atualiza a variável 'maior_elemento'
            maior_elemento = numero

    # Retorna o maior elemento encontrado após percorrer toda a lista
    return maior_elemento


# --- Exemplo de uso ---[cite: 1]
lista_exemplo = [7, 2, 5, 1, 4, 3, 6]  # Define uma lista de teste[cite: 1]

# Chama a função passando a lista de exemplo e guarda o resultado[cite: 1]
maior_elemento = encontrar_maior_elemento_iterativo(lista_exemplo)

# Exibe o resultado da busca no console[cite: 1]
print(f"O maior elemento da lista é: {maior_elemento}")