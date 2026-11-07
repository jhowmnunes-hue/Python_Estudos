###entrada_e_saida_de_dados_calculadora_pedidos_caixa_lanchonete
#entrada de dados
hamburguer = 10.50
batata_frita = 4.00
refrigerante = 3.00

#entrada de dados do usuário
quantidade_hamburguer = int(input("Digite a quantidade de hambúrgueres desejados: "))
quantidade_batata = int(input("Digite a quantidade de batatas fritas desejadas: "))
quantidade_refrigerante = int(input("Digite a quantidade de refrigerantes desejados: "))

#Cálculo do preço total
preco_total = (hamburguer * quantidade_hamburguer) + (batata_frita * quantidade_batata) + (refrigerante * quantidade_refrigerante)

#Saída de dados
print("O preço total do seu pedido é: R$", preco_total)

####Exemplo execuçao do programa
#Digite a quantidade de hambúrgueres desejados: 2
#Digite a quantidade de batatas fritas desejadas: 1
#Digite a quantidade de refrigerantes desejados: 3
#O preço total do seu pedido é: R$ 34.0