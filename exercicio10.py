# 1. Entrada de dados em uma lista
lista = []
listamaiorquemedia=[]
soma = 0

for i in range(20):
    numero = float(input(f"Digite o {i+1}º número real: "))
    lista.append(numero)
    soma += numero

# 2. Cálculo e exibição da média
media = soma / 20
print(f"\nA média dos números é: {media:.2f}\n")

# 3. Identificação dos elementos maiores que a média
for numero in lista:
    if numero > media:
        listamaiorquemedia.append(numero)
print(f"Elementos maiores que a média:\n{listamaiorquemedia}")