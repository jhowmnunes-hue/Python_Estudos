escolha = input("Escolha uma opção de função 1 ou 2: ")
if escolha == "1":
    def func1(x):
        return x + 1
    s = func1(10)
    print(s)
else:
    def func2(x):
        return x + 2
    s = func2(10)
    print(s)

###Cada subprograma tem um único ponto de entrada, que é onde sua execução começa.
###Quando um subprograma é chamado, o programa chamador é suspenso até que o subprograma termine sua execução.
###Após a execução do subprograma, o controle sempre retorna ao ponto de chamada no programa chamador.
