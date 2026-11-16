# -Funções recursivas na prática
#
# -O problema das Torres de Hanói é um quebra-cabeça matemático e de lógica
# que envolve a movimentação de discos entre três pinos ou torres.
#
# -O problema envolve uma base de pinos verticais, em que os discos estão
# inicialmente empilhados em ordem crescente de tamanho em um dos pinos,
# com o disco menor no topo e o disco maior na base.
#
# -O objetivo do problema é mover todos os discos da torre de origem para
# a torre de destino, usando a torre auxiliar, de forma que os discos permaneçam
# empilhados em ordem crescente de tamanho em todos os momentos e que apenas
# um disco seja movido por vez. Além disso, em nenhum momento um disco maior
# pode ser colocado sobre um disco menor.
#
# -Escreva uma função em Python para resolver as Torres de Hanói de forma recursiva.

def mover_disco(origem, destino):
    disco = origem.pop()     # .pop() remove e retorna o último item da lista
    destino.append(disco)    # .append() insere um item no final da lista

def imprimir_torres(torre_A, torre_B, torre_C):
    print("A:", torre_A)
    print("B:", torre_B)
    print("C:", torre_C)
    print()

def torres_de_hanoi_recursivo(num_discos, origem, destino, auxiliar):
   if num_discos == 1:
        mover_disco(origem, destino)
        imprimir_torres(torre_A, torre_B, torre_C)
   else:
        torres_de_hanoi_recursivo(num_discos - 1, origem, auxiliar, destino)
        mover_disco(origem, destino)
        imprimir_torres(torre_A, torre_B, torre_C)
        torres_de_hanoi_recursivo(num_discos - 1, auxiliar, destino, origem)

# Resolvendo o problema recursivamente
num_disco = 3
# Inicializando as torres e os discos
torre_A = list(range(num_disco, 0, -1)) # Cria a lista: [3, 2, 1]
torre_B = []                            # Cria uma lista vazia: []
torre_C = []                            # Cria uma lista vazia: []
# Mostrando o estado inicial
imprimir_torres(torre_A, torre_B, torre_C)
torres_de_hanoi_recursivo( num_disco, torre_A, torre_C, torre_B)
