numeros=[]
print(type(numeros))
numeros=[10,23,-89,39]
print(numeros)
primer_elemento=numeros[0]
print(f"primer elemento:{primer_elemento}")
print(len(numeros))
#recorrer la lista
for elem in numeros:
    print(elem, end=", ")
print()
#agregar un elemento a la lista
numeros[len(numeros)-1]=100
print(numeros)
numeros[-1]=110
print(numeros)
#no estamos sobreescribiendo el ultimo que no existe
#numeros[4]=120
#print(numeros)
numeros.append(4)
print(numeros)
lista_regalos=["medias","vino","perfume"]
print(lista_regalos)
lista_regalos.append(["remera","galletas","carbon"])
print(lista_regalos)
#insert
numeros.insert(1,-23)
print(numeros)
#index
indice=numeros.index(110)
print(f"indice{indice}")
#lista con range
lrange=list(range(7))
print(lrange)
#remove
lrange.remove(3)
print(lrange)
#reverse
lrange.reverse()
print(lrange)
#count
lrange.append(2)
print(lrange)
#sum, min, max
print(min(lrange))
#del
del(lrange [2])
print(lrange)

numeros=[1,2,3],[4,5,6],[7,8,9]
for i in range(len(numeros)):
    for j in range (len(numeros)):
        print(numeros [i][j]) 

for fila in numeros:
    for elementos in fila:
        print(elementos, end=",")        
    print()    
