def func1():
    global x
    x = 10
    print(f"Função func1 - x = {x}")


def func2():
    global x
    x = 20
    print(f"Função func2 - x = {x}")

x = 0
print(f"Programa principal - x = {x}")
func1()
print(f"após func1 - x = {x}")
func2()
print(f"após func2 - x = {x}")



# 1. A variável 'x' nasce no programa principal valendo 0 (x = 0).
# 2. A palavra 'global x' dentro das funções dá uma permissão especial:
#    em vez de criar uma variável local só da função, ela autoriza a função
#    a mexer e alterar diretamente a variável 'x' lá de fora.
#
# Passo a passo do que acontece neste código:
# - Começa: x = 0
# - Roda func1(): usa 'global x' e altera o valor de fora para 10.
# - Roda func2(): usa 'global x' e altera o valor de fora para 20.
#
# Conclusão: Com 'global', a função muda a variável de fora diretamente,
# sem precisar usar 'return' nem o sinal de igual (x =) ao chamar a função.