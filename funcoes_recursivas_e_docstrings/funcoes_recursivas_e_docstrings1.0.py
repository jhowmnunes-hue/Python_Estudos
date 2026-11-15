### Funções recursivas e docstrings
# Função recursiva é uma função que chama sí proprio para exercutar alguma coisa.
# Muitas atividades podemos fazer de forma iterativa ou usando recursao.
# as vezes a recursao fica muito mais simples do que de forma iterativa.



# Função recursiva contagem regressiva
def regressiva(x):
    print(x)
    if x > 0:
        regressiva(x - 1)
    else:
        print('acabou')
regressiva(10)

# Não recursiva (nao é uma função é apenas o for)
for y in range (10 ,-1, -1):
    print(y)
print('acabou')
