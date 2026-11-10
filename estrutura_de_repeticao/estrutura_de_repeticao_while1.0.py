###estrutura_de_repeticao_while1.0
#Em portugues while é enquanto.
#É Executado enquanto a condição é verdadeiro
#quando a condição é falsa ele sai.
#while testa antes de entrar

print("antes while")
palavra = input("Entre com a palavra:")
while palavra != "sair":
    print ("dentro while")
    palavra = input("Digite sair para encerrar o laço:")
print("Você digitou sair e agora está fora do laço")