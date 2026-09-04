matriz = [] 
#criação  e preenchjimento da matriz
for i in range (3):
    linha = []
    for j in range(3):
        valor = int(input(f"digite o valor par a aposição {i}{j} da matriz:"))
        linha.append(valor)   
    matriz.append(linha)

#diagonal principla é a parte da matriz onde os numeros de i e j são iguais.
#ex: 00 11 22 etc.

#bloco que realiza a soma dos numeros acima da diagonal principal
soma = 0    
for i in range(3):
    for j in range(3):
        if j > i:
            soma += matriz[i][j]
            
# aprensenta a matriz que o usuario digitou.
print("________MATRIZ DO USUARIO_______")

for linha in matriz:
    print("[", end=" ")
    for valor in linha:
        print(f"{valor:4}", end=" ")
    print("]")
    
print(f"A soma dos números acima da diagonal principal é: {soma}")