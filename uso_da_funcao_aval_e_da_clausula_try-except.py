### uso_da_funcao_aval_e_da_clausula_try-except

def calculadora_expressao():
    # Solicitar ao usuário que insira uma expressão matemática
    expressao = input("Digite uma expressão matemática ")

    try:
        # Avaliar a expressão usando eval
        resultado = eval(expressao)
        print("O resultado da expressao é:", resultado)
    except Exception as e:
        print("Erro ao avaliar a expressao:", e)

#chamar a função
calculadora_expressao()
#Exemplo da chamada do programa:
#Digeite uma expressao matemática: 2 + 3 * (4 - 1)
#O resultado da expressao é: 11