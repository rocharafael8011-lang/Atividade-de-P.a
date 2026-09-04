numeros = []
vContNumPar = 0
vContNumImpar = 0

#bloco que insere os valores das posições i da lista
for i in range (20):
    valor = int (input(f"digiote o valor da posição {i+1} da lista:"))
    numeros.append(valor)

#parte que calcula qual numero é par e adiciona masi um a variavel se for par ou impar
for numero in numeros:
    if numero % 2 == 0:
        vcontNumPar +=1
    else:
        vContNumImpar += 1
#exibição dos resultados do calculo
print(f"Quantidade de pares: {vContNumPar}")
print(f"Quantidade de ímpares: {vContNumImpar}")