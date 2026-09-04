numeros = []

#bloco que insere os valores das posições i da lista
for i in range (0,11):
    valor = int (input(f"digiote o valor da posição {i+1}° da lista:"))
    numeros.append(valor)
# fazendo a soma com metodo pronto.
somacincoPrimeiros = sum(numeros[:5])
somacincoUltimos = sum(numeros[5:])

#contador = 0
#somacincoPrimeiros = 0
#somacincoUltimos = 0

# realiza a soma de forma 100% na logica pura sem metodo pronto
#for numero in numeros:
#    if contador < 5:
#        
#        somacincoPrimeiros+=numero
#        
#    elif contador > 5:
#        
#        somacincoUltimos+=numero
#        
#    contador+=1

print(f"A sioma dos 5 primeiros numeros é: {somacincoPrimeiros}")
print(f"A sioma dos 5 ultimos numeros é: {somacincoUltimos}")
