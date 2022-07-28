#Escriba un código que permita ingresar los datos numéricos enteros correspondientes a un experimento de
#laboratorio. Como no se sabe cuántos son los datos a ingresar, el usuario deberá ingresar primero la
#cantidad máxima de datos posibles (valor comprendido entre 0 y 100). Como los datos que se van a ingresar
#son todos positivos, el ingreso de datos del lote también puede finalizar por el ingreso de un numero
#negativo (la finalización se producirá por lo primero que suceda). Indicar por consola. Luego se pide que se
#calcule el promedio con precisión decimal de 2 dígitos. Informe el resultado por pantalla.

indice = int(input("Ingrese la cantidad de números que desea analizar: "))

while indice<=0 or indice>=100:
    print("La cantidad ingresada es incorrecta. Ingrese nuevamente la cantidad de números: ")
    indice=int(input())
    
listaDatos = []
sumaNum = 0

for numero in range(0,indice): 
    numero2=int(input(f'Ingrese el numero {numero + 1}: '))
    sumaNum += numero2
    listaDatos.append(numero2)
    
    if numero == (indice-1):
        print("Se ha terminado el ingreso. Los datos son los siguientes: ")
        for numero in range(0,indice):
            print(f'El valor del dato {numero + 1} es {listaDatos[numero]}')
        promedio = round(sumaNum/indice,2)
        print(promedio)
    
    elif listaDatos[numero] < 0:
        numero3=numero
        print("Termino el ingreso de datos. Los datos ingresados son los siguientes: ")
        for numero4 in range(0,numero3):
            print(f'El valor del dato {numero4 + 1} es {listaDatos[numero4]}')
        promedio = round((sumaNum-listaDatos[numero3])/(numero3),2)
        print(promedio)
        break     
    
             

        