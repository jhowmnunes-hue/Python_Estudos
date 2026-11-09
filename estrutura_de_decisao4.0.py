###Estrutura de decisão

vnr = eval(input("Digite um número:"))
print("valor digitado", vnr)
print("antes do if")
if vnr <= 100:
    print("entrou no if do 100")
elif vnr <= 500:
    print("entrou no elif do 500")
elif vnr <= 1000:
    print("entrou no elif do 1000")
else:
    print("entrou no else")
print("saiu do if")

#Neste código, se o if falhar ele vai fazer o elif.
#se o elif funcionar ele vai apresentar o print da linha 9.
#se o teste falhar ele cai no else.
#por exemplo, digitando 80 é menor que 500 mas vai executar o if primeiro, pois no momento que a condição der verdadeiro não vai executar mais

#if: verdadeiro = estrutura de seleção
#else: falso = condição onde o if não é atendida
#elif: If dentro do outro if mas não é identado, nao esta dentro do if e nem do else, ele é um teste no meio

