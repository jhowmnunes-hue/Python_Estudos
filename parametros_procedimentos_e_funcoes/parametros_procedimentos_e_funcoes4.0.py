def func1(x):
    x = 10
    print(f"Função funcc1 - x = {x}")

def func2(x):
    x = 20
    print(f"Função func2 - x = {x}")

x = 0
print(f"Programa principal - x = {x}")
func1(x)
print(f"após func1 - x = {x}")
func2(x)
print(f"após func2 - x - {x}")


# -Sem 'return': As funções não devolvem nenhum resultado para fora.
# -Sem sinal de igual (=): Chamamos apenas func1(x) e func2(x), sem o 'x ='
# na frente para receber e atualizar o valor.

# Conclusão: O 'x = 10' e 'x = 20' existem apenas dentro de cada função (escopo local).
# A variável 'x' do programa principal continua intacta valendo 0 até o final.