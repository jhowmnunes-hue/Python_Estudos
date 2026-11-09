# formatação de dados de saída
#pode utilizar a função print() e função format()
#Para tornar a saída formatada ainda mais intuitiva, basta utilizar a letra ‘f’ no início dos parâmetros da função print() e colocar cada variável dentro das chaves na posição em que deve ser impressa.
#Ele permite que a chamada à função print() fique muito parecida com as chamadas à função printf() em C, com passagem de parâmetros a serem colocados em ordem na string. 
#Com o método format(), podemos montar a string com as chaves {} indicando onde entrarão valores, passados como parâmetros separados por vírgulas

### Exemplo de código em python:
#defirni variáveis
nome = "João"
idade = 25
altura = 1.75

#formatação usanto f-string (python 3.6+)
saida_formatada = f"Nome: {nome}, Idade: {idade}, Altura: {altura:.2f}m"

# Exibir a saída formatada
print(saida_formatada)

###exemplo de saída:
#Nome: João, Idade: 25, Altura: 1.75m
