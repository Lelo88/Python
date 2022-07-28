#Codifique un programa que calcule los factores de un número ingresado por el usuario, y muestre el
#resultado por pantalla.

numero = int(input("Ingrese un número: "))

while numero<=1:
    print("No le corresponde una factorización. Ingrese un número: ")
    numero = int(input("Ingrese un número: "))

print(f'El factoreo del número {numero} es: ')

n=2
factores = []
while numero > 1: 
    while numero % n == 0:
        numero/=n
        if numero>1:
            factores.append(n)
        else:
            factores.append(n)    
    n+=1
    
factores2 = ' x '.join(str(num) for num in factores)
print(factores2)    