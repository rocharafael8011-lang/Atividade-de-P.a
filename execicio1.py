numeros = []
total = 0
for i in range (5): 
    numero = float(input(f"digite o valor da {i+1}° nota:"))
    numeros.append(numero)

print(f"As notas do aluno são {numeros}")

for i in numeros:
    total+=i

mediaNota = total / 5

if mediaNota >= 7.0 :
    print(f"O alunoi esta aprovado!")
elif mediaNota >=5.0:
    print(f"o aluno esta de recuperação")
else:
    print(f"ALuno reprovado")