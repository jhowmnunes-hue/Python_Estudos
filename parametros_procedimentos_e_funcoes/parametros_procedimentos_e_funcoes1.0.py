def calcula_imc (peso, altura):
    return peso * 100 / (altura * 2) #calculo da massa corporal #peso por 100 para trabalhar com altura em cm e nao metros
                                     #caso contrario, teria que trabalhar com ponto flutuante
peso = eval(input("digite o peso em quilos")) #input recebe o dado como testo #eval joga como numero inteiro
altura = eval(input("digete a altura em centimetros"))
calcula_imc(peso, altura)
imc = calcula_imc (peso, altura) #estou chamando a funcao
print ("imc = ", imc)

