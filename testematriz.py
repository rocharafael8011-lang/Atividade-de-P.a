matriz = []

for i in range (3):
    linhaMatriz = []
    
    for j in range(3):
        valor=int(input(f"difite o valor para a posição {i} e {j} da matriz:"))
        linhaMatriz.append(valor)
    matriz.append(linhaMatriz)
        
#for i in range (3):
    #for j in range(3):
        #print(matriz[i][j], end=" ")
    #print()
    
for linha in matriz:
    print("[", end=" ")
    for valor in linha:
        print(f"{valor:3}", end=" ")
    print("]")