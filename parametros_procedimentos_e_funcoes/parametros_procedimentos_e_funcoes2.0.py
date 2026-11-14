def taximetro(distancia, multiplicador=1): #(parametro entrada, parametro entrada entrada)
    largada = 3
    km_rodado = 2
    valor = (largada + distancia *
    km_rodado) * multiplicador
    return valor

pagamento = taximetro(3.5, 2) #Assumiu o parametro default (distancia, multiplicador
print(pagamento)


# O parâmetro multiplicador tem um valor padrão(default) de 1.
# Isso significa que, se não passarmos um valor para multiplicador ao chamar a função, ele usará 1 como padrão.
# Quando chamamos taximetro(3.5), a função usa multiplicador=1 por padrão.

# A palavra reservada "return" indica que a função retorna algum valor.
# Isso implica que o valor retornado seja armazenado em uma variável do programa chamador (como ocorre na linha 8) ou utilizado como parâmetro para outra função.