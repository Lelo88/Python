#Utilizando datos tipo struct, estructuras de control de flujo switch case y funciones,
#escriba un algoritmo que permita cargar los socios de un club (máximo 100 socios).  La información de cada socio será: nombre, apellido, no documento, fecha de
#nacimiento, edad (la cual se debe calcular automáticamente a partir de la fecha de
#nacimiento, se puede ayudar con time.h), y un número de socio (distinto al DNI)
#generado automáticamente.  La interfaz de programa debe ser a través de un menú, donde el usuario pueda
#elegir entre ingresar datos, ver los datos cargados, o salir del programa.  Al estar en la etapa de ingreso de datos, se debe solicitar de manera secuencial
#cada uno de los datos de cada socio. Es decir, para el primer socio solicitar cada
#uno de los datos mencionados, luego pasar al segundo socio, etc., hasta que el
#usuario decida finalizar la carga ingresando un DNI negativo.  Al finalizar la carga se debe regresar al menú principal, y desde ahí el usuario
#debe poder elegir si desea ingresar más socios, ver los socios ya cargados, o salir
#del programa.

import os

lista = list()

class Socio: #definicion tipo estructura de C en Python
    cantSocio=1
    def __init__(self, nombre, apellido, dni, numSocio, fechNac, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.numSocio = numSocio
        self.fechNac = fechNac
        self.edad = edad
         
        
def menu():
    opciones = {
        '1': ('Carga de datos', ingresoDatos),
        '2': ('Visualizar datos',verDatos),
        '3': ('Salir del programa', salida)
    }
    generarMenu(opciones, '3')
    
def generarMenu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:    
        muestraMenu(opciones)
        opcion = leerOpcion(opciones)
        ejecutaOpcion(opcion,opciones)
    
def muestraMenu(opciones):
    os.system("cls")
    print('Seleccione una opción: ')
    for clave in sorted(opciones):
        print(f'{clave}){opciones[clave][0]}')
        
def leerOpcion(opciones):
    while(a:=input('Opcion: ')) not in opciones:
        print('Opcion incorrecta. Vuelva a intentarlo.')
    return a   

def ejecutaOpcion(opcion,opciones):
    opciones[opcion][1]()

def ingresoDatos():
    os.system("cls")
    print("-------- INGRESO DE DATOS ------")
    print()
    ingreso = Socio(input("Ingrese el nombre: "),input("Ingrese el apellido: "),
    int(input("Ingrese el número de DNI. Ingrese un número negativo para dejar de ingresar")),
    input("Ingrese la fecha de nacimiento: "),int(input("Ingrese la edad: ")),input("Ingrese el numero de socio: "))    
    
    lista.append(ingreso)
    
    if ingreso.dni<0:
        lista.remove(ingreso)
        
    
def verDatos():
    os.system("cls")
    print("------- VISUALIZACION DE DATOS ------")
    for datos in lista:
        cantSocio = 1
        print(f'Datos del socio {cantSocio}')
        print(f'DNI: {datos.dni} Numero de socio: {datos.numSocio}\n')
        print(f'Nombre: {datos.nombre} Apellido: {datos.apellido}\n Edad: {datos.edad} Fecha de nacimiento: {datos.fechNac}')
        cantSocio += 1
    os.system("pause")
    
def salida():
    os.system("cls")
    print("Usted está saliendo del programa. ¡Hasta luego!")             
    
if __name__=="__main__":
    menu()    