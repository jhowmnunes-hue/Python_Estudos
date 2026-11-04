# Solicita ao usuário que insira as três notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
 
# Calcula a média das notas
media = (nota1 + nota2 + nota3) / 3
 
# Mostra o resultado ao usuário
print(f"A média das notas é: {media:.2f}")


# Solicitamos ao usuário que insira as três notas, utilizando a função input.
# Convertemos esses valores para o tipo float, pois a entrada padrão do input é uma string.
# Calculamos a média das notas utilizando a fórmula (nota1 + nota2 + nota3)/3.
# Exibimos o resultado da média ao usuário com duas casas decimais utilizando a formatação de string :.2f. 