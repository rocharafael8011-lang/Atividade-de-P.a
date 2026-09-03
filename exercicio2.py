numeros = []
vcontnegativos = 0 
somapositivos = 0

for i in range (0,20):
    numero = float(input(f"insira oo valor da posição {i+1}° da lista:"))
    numeros.append(numero)
for n in numeros:
    if n < 0: 
        vcontnegativos +=1
    elif n > 0 :
        somapositivos += n
        
print(f" o valor da soma dos numeros positivos é: {somapositivos}")
print(f"A quantidade de numeros negativbos na lista é: {vcontnegativos}")