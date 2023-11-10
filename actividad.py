lenguaje = "python"
letra = "t"

if letra in "python": 
    print(f"la letra {letra} esta en la cadena python")
else:
    print("no esta")

"""
nota1 = 7
nota2 = 8
nota3 = 10

promedio = (nota1+nota2+nota3)/3
print(f"el promedio de {nota1},{nota2},{nota3}, es {promedio:.2f}")

"""
cont = 0
while cont <= 10:
    print(cont)
    cont=cont+1

cont = int(input("ingrese numero"))
while cont <= 10:
    print(cont)
    cont=cont+1"""


promedio = 0
cont = 0
suma = 0
while (cont <3):
    nota = int(input("ingrese nota "))
    suma = suma+nota
promedio = suma /cont
print(f"el proimedio es {promedio}")        
