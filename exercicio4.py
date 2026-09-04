matriz = []
vcontNumerosMaiorQueDez = 0 
for i in range (3):
    linha = []
    for j in range(3):
        valor = int(input(f"digite o valor par a aposição {i}{j} da matriz:"))
        linha.append(valor)
    
        if valor > 10:
            vcontNumerosMaiorQueDez +=1
        
    matriz.append(linha)
print("________MATRIZ DO USUARIO_______")

for linha in matriz:
    print("[", end=" ")
    for valor in linha:
        print(f"{valor:4}", end=" ")
    print("]")
    
print(f"A qunridade de numeros maiores que dez dentro da matriz é: {vcontNumerosMaiorQueDez}")