#Desarrolle una función que permita ordenar los datos de un vector de menor a mayor, o de mayor a menor,
#según lo indique el usuario. Luego, escriba un programa donde se utilice esta función.

def menu():
    opciones = {
        '1': ('Ordena de menor a mayor', ordenaMayor),
        '2': ('Ordena de mayor a menor', ordenaMenor),
        '3': ('Salida', salida)
    }
    generaMenu(opciones, '3')
    
def generaMenu(opciones, opcion_salida):
    listado=ingreso()
    opcion = None
    while opcion != opcion_salida:
        mostrarMenu(opciones)
        opcion = leerOpcion(opciones)
        ejecutarOpcion(opcion, opciones,listado)
        print()
        
def mostrarMenu(opciones):
    print('Seleccione una opción: ')
    for clave in sorted(opciones):
        print(f'{clave}){opciones[clave][0]}')
        
def leerOpcion(opciones):
    while(a:=input('Opcion: ')) not in opciones:
        print('Opcion incorrecta. Vuelva a intentarlo.')
    return a

def ejecutarOpcion(opcion, opciones,listado):
    if opcion=='1'or opcion == '2':
        opciones[opcion][1](listado)
    elif opcion=='3':
        opciones[opcion][1]()                   
            
def ordenaMayor(numeros):
    print(" ".join(sorted(str(n) for n in numeros)))
 

def ordenaMenor(numeros):
    print(" ".join(sorted((str(n) for n in numeros),reverse=True)))

def salida():
    print("Usted esta saliendo del programa. Hasta luego!")    
     
def ingreso():
    numero=int(input("Ingrese la cantidad de numeros que desea ingresar: "))
    while numero<=0 or numero>=100:
        print("La cantidad de ingresos es incorrecta. Ingrese una cantidad permitida: ")
        numero=int(input("Ingrese la cantidad de numeros que desea ingresar: "))
    
    listado=[]
    for num in range(0,numero):
        numeroAgregado=int(input(f'Número {num+1}: '))
        listado.append(numeroAgregado)
    return listado          
            
if __name__ == "__main__":
    menu()            