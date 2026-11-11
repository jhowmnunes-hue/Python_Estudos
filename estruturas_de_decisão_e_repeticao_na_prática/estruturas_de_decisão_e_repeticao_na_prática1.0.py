###  ****Estruturas de decisão e repetição na prática****


#Fazer um programa em python para descobrir todos os numeros entre 1000 e 9999.
#Cujo a raiz quadrada seja igual a soma do número formado
#Pelos 2 algarismo mais significativos e 2 algarismomos menos significativos

for num in range (1000,10000):
    menor = num % 100 #obtem o numero dos algarismos menos significativos
    maior = num // 100 #obtem o numero dos alagarismos mais significativos
    raiz = menor + maior #obtem a raiz
    
    if (raiz * raiz ) == num: #valida se a raiz gera o numero testado
        print(num)
        print(menor)
        print(maior)
        print(raiz)
print("terminou")
print("saiu ", num)
    
#EXEMPLO 1: NÚMERO 2465

#                24: os 2 números a esquerda são os mais significativos
#                65: os 2 números a esquerda são os menos significativos
#                89: É a soma entre eles.

# Se 89 for a raiz quadrada de 2465 - esse número 2465 é para voltar
# Caso contrario não é pra voltar

# // é divisao inteira
# % é o restante da divisao

#EXEMPLO 2: NÚMERO 2897

# 2897 / 100 = 28,97 (sobra o 97, desta forma obtive os 2 numeros menos significativos)
# 28*100 = 2800

