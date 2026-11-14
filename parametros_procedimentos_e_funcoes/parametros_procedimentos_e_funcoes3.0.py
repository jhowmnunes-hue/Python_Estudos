def func1(x):
    x = 10 #escopo local (só existe dentro desta funcao)
    print(f"Função funcc1 - x = {x}")

def func2(x):
    x = 20 #escolo local (so existe dentro desta funcao)
    print(f"Função func2 - x = {x}")
    return x #devolve o valor de x para quem chamou a função

vn = 0
print(f"Programa principal - vn = {vn} \n") #imprimindo o valor da variavel "vn"
vn = func1(vn) # Chama a func1 e guarda o resultado em vn (como não tem return na funcao 1, vn vira None)
print(f"Programa principal - vn = {vn} \n") # Mostra None, pois a func1 não retornou nada
vn = func2(vn) # Chama a func2, que retorna x (20), e guarda em vn
print(f"Programa principal - x = {vn} \n") # Mostra o novo valor de vn (20)














# ==========================================
# RESUMO: O QUE SIGNIFICA "GUARDAR EM vn"?
# ==========================================
# O sinal de igual (=) é o responsável por "guardar" as coisas.
#
# 1. Quando fazemos: vn = func1(vn)
#    - A func1 roda, mas NÃO tem o comando 'return'.
#    - REGRA: Sempre que uma função não tem 'return', ela retorna 'None'.
#    - O sinal '=' pega esse 'None' e GUARDA dentro da variável 'vn'.
#    - o novo valor de vn passa de 0 para "none"
#
# 2. Quando fazemos: vn = func2(vn)
#    - A func2 roda e TEM o comando 'return x' (que vale 20).
#    - O sinal '=' pega esse '20' e GUARDA dentro da variável 'vn',
#      fazendo o 'vn' passar de 0 para 20.
#    - Ele pega o valor da funçao e atualiza o valor da variavel

# ==========================================
# O QUE SIGNIFICA COLOCAR A VARIÁVEL NOS PARÊNTESES?
# ==========================================
# Quando escrevemos func1(vn):
# - Estamos apenas PEGANDO uma cópia do valor de 'vn' (por exemplo, 0)
#   e entregando para a função.
# - MAS ATENÇÃO: a função NÃO FICA com esse valor!
# - Logo na primeira linha lá dentro, a função substitui esse valor
#   pelo valor próprio dela (x = 10 ou x = 20).
#
# Resumo completo do processo:
# 1. O que está nos parênteses (vn) = ENVIAR valor para a função.
# 2. O sinal de igual (vn =) = GUARDAR o resultado que a função devolveu na variavel.