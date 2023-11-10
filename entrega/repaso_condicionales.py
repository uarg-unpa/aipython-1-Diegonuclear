num1=int(input("ingrese numero 1"))
num2=int(input("ingrese numero 2"))
num3=int(input("ingrese numero 3"))
producto=num1*num2*num3
suma=num1*num2*num3
print(f"la suma es {suma} y el producto es{producto}")           


num=int(input("ingrese numero"))
cont=1
suma=0
producto=1
while cont<=3:
    suma=suma+num
    producto=producto*num
    cont=cont+1
print(f"la suma es {suma} y el producto es{producto}")


num=0
cont=0
mayor=0

while cont <6:
    num=int(input("ingrese numero"))
    if num > mayor:
        mayor=num
    cont=cont+1
    