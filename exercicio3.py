numeros = []

index = 0

for i in range (0,9):
    numero = int(input(f"insira o valor da posição {i+1}° da lista:"))
    numeros.append(numero)
vMaiorAtual = numeros[0]
for indice in range(1, len(numeros)):
    if numeros[indice] > vMaiorAtual:
        vMaiorAtual = numeros[indice]
        posicaoMaior = indice
        
print(f"A lista digitada foi: {numeros}")
print(f"O maior valor armazenado é: {vMaiorAtual}")
print(f"Ele está na posição de índice: {posicaoMaior} (Ou seja, é o {posicaoMaior + 1}º número da lista)")