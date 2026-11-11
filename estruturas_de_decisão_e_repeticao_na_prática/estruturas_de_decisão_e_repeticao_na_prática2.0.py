###  ****Estruturas de decisão e repetição na prática****


#Fazer um programa em python para descobrir todos os numeros entre 1000 e 9999.
#Cujo a raiz quadrada seja igual a soma do número formado
#Pelos 2 algarismo mais significativos e 2 algarismomos menos significativos

for raiz in range (32,100):
    num = raiz * raiz #caçcula o numero gerado pela raiz
    menor = num % 100 #obtem o numero dos algarismos menos significativos
    maior = num // 100 #obtem o numero dos algarismos mais significativos
    
    if (menor + maior) == raiz: #valida se a raiz corresposde a soma
        print(num)
        print(menor)
        print(maior)
        print(raiz)
print("terminou")
print("saiu ", num)


#Dica para exercicio: caracteristica, se a raiz é a soma de 2 números inteiros...
#A raiz quadrada deve ser um número inteiro.
#Não precisa testar todos o números.
#Sabemos disso partindo da raiz e não dos números


### EXEMPLO: 32*32 = 1024
#DE 1024 EXTRAI O 10
#DEPOIS EXTRAI O  24
#SOMA OS 2 =      34
#VERIFICO SE ESSE NÚMERO É IGUAL AO QUE COMEÇOU.
#SE 34 FOR IGUAL AO 32 - O NUMERO VOLTA (O NUMERO QUADRADO)