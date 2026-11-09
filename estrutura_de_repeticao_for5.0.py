### Estrutura de repetição: for
#for é uma instrutura de repetição baseada em contagem

numeros = [1, 2, 3, 4, 5]
soma = 0
for numero in numeros:
    soma += numero
print(f"A soma de todos números é {soma}")


#o print esta fora da identação do for, ele vai ser executado após a soma de todos os números entao é impresso somente uma vez
#caso esteja dentro do loop ele vai somando e imprimindo a cada leitura
