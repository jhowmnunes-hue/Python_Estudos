###estrutura_de_repeticao_while2.0
#Em portugues while é enquanto.
#É Executado enquanto a condição é verdadeiro
#quando a condição é falsa ele sai.
#while testa antes de entrar

print("antes while")
palavra = input("Entre com uma palavra:")
while palavra != "sair":
    print ("dentro while")
    palavra = input("Digete sair para encerrar o laço:")
print ("Você digitou sair e agora está fora do laço")

#como while testa antes, se digitar direto sair, o teste vai falhar e vai direto para depois do loop
