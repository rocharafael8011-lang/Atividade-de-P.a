listanumeros = []

for i in range (10):
    num = int(input(f"digite o numero que sera inserido na posição {i+1}° da lista:"))
    listanumeros.append(num)

Somaatevinte = 0
SomaateTrinta = 0
SomaMaiorQuetrinta = 0

for numero in listanumeros:
    if numero <= 20:
        Somaatevinte += numero
    elif numero <= 30:
        SomaateTrinta += numero
    else:
        SomaMaiorQuetrinta += numero
    
print("________RESULTADO_______")

print(f"A soma dos numeros até vinte é :{Somaatevinte}")
print(f"A soma dos numeros menores ou iguais a 30 é:{SomaateTrinta}")
print(f"A soma dos nuemros maiores que trinta é: {SomaMaiorQuetrinta}")