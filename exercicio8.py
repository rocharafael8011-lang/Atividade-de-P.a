import random
#criando a lista com os 50 valores aleatorios
lista = [random.randint(1,51) for _ in range(50)]
#print(lista)
#pedidindo ao usuario que numero ele deseja encontrar na lista
busca = int(input(f"digite o valor que deseja procurar dentro da lista:"))

encontrado = False

#bloco que verifica se o numero inserido esta dentro da lista ou não
for numero in lista:
    if numero == busca:
        encontrado = True
        break
#apresenta a lista
print(lista)
#apresenta a mesnagem de acordo com o resultado
if encontrado:
    print(f"O número {busca} ESTÁ na lista!")
else:
    print(f"O numero {busca} NÃO esta na lista")