#Codifique un programa que:
#Solicite al usuario el ingreso de 50 números enteros. Luego de ingresados todos estos,
#informe al final:  Cantidad de números impares ingresados  El promedio de los números pares ingresados
#cuales fueron los numeros maximos y minimos
#El porcentaje de numeros menores que 50

from audioop import reverse


numeros=[]
cantNumImp=0
cantPar = 0
pares = 0
promPar = 0
cant50 = 0
sumaNum50 = 0 
promMen50 = 0 

for numero in range(0,5):
    numero=int(input(f'Ingrese el numero {numero + 1}: '))
    
    if numero%2 !=0:
        cantNumImp+=1
    
    if numero%2==0:
       cantPar+=1
       pares+=numero        
    
    if numero<50:
        cant50 += 1
        sumaNum50 += numero 
    
    numeros.append(numero)
    
promPar = round(pares/cantPar,2)
promMen50 = round(sumaNum50/cant50,2)
numeros2= ' '.join(sorted(str(n) for n in numeros)) #como los numeros estan en una lista los uno en un join de forma separada

print(f'Los números ingresados son: {numeros2}')
print(f'La cantidad de impares es de: {cantNumImp}')
print(f'El promedio de los pares es: {promPar}')    
print(f'El menor de todos los numeros ingresados es: {min(numeros)}')
print(f'El mayor de todos los numeros ingresados es: {max(numeros)}')
print(f'El promedio de los numeros ingresados menores a 50 es de: {promMen50}')    

