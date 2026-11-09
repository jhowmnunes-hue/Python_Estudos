#Atribuição_Entrada_e_Saida_de_dados_na_pratica

#Atribuição de valores a variáveis
nome = "Alice"
idade = 30
#entrade da dados do usuario
altura = float(input("Digite a sua altura em metros: "))
peso = float(input("Digeite o seu peso em kg: "))
# Cálculo do IMC (Indice de Massa Corporal)
imc = peso / (altura ** 2) # ** significa que esta calculando altura ao quadrado
# Saída de dados formatada
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Altura: {altura:.2f}m")
print(f"Peso: {peso:.1f}kg")
print(f"IMC: {imc:.2f}")


###Exemplo de Saída:
# Digite a sua altura em metros: 1.75
# Digite o seu peso em kg: 68
# Nome: Alice
# Idade: 30
# Altura: 1.75m
# Peso: 68.0kg
# IMC: 22.20
