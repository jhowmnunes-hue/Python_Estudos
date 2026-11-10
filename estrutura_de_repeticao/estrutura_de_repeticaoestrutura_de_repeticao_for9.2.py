#Para entender a diferença entre break e continue, vamos modificar o exemplo anterior substituindo continue por break e ver o que acontece.
#Essa alteração está no arquivo disponibilizado (código 9).

for num in range(1, 11):
    if num == 5:
        break
    else:
        print(num)
print('Laço encerrado')
