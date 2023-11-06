num=0
cont=0
menor=1

while cont <6:
    num=int(input("ingrese numero"))
    if num <= menor:
        menor=num
    cont=cont+1
print (f"el menor de los numeros es {menor}")    