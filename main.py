# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def print_menu_opciones():
    print("Proyecto de programacion y algotitmos\n")
    print("Calculadora química\n\n")
    print("\tMenu de opciones:")
    print("\t\t1)\tCalculadora de masa molar\n")
    print("\t\t2)\tCalculadora de ley de gases\n")
    print("\t\t3)\tConsulta de elemento de tabla periodica\n")
    print("\t\t4)\tCalculadora de conversiones\n")
    print("\t\t5)\tTerminar programa\n")


def menu_temperatura():
    print("\tMenu de opciones de conversion de temperatura:")
    print("\t\t1)\tConvertir de C -> F")
    print("\t\t2)\tConvertir de C -> K")
    print("\t\t3)\tConvertir de F -> C")
    print("\t\t4)\tConvertir de F -> K")
    print("\t\t5)\tConvertir de K -> C")
    print("\t\t6)\tConvertir de K -> F")


def conversion_celsius(a, b):
    #a selecionador si F o K
    if a == 1: #Covnvertir celsius a F
        return (9/5) * b + 32
    else: #Covnvertir celsius a K
        return b + 273.15


def conversion_farenheit(a, b):
    #a selecionador si F o K
    if a == 1: #Covnvertir F a C
        return (b - 32)/1.8
    else: #Covnvertir F a K
        return (b + 459.67)/1.8

def conversion_kelvin(a, b):
    #a selecionador si F o K
    if a == 1: #Covnvertir K a C
        return b - 273.15
    else: #Covnvertir k a F
        return b * 1.8 -459.67


def calcular_conversion_temp():
    menu_temperatura()
    opcion_menu_t = int(input("Introduce la opcicion a convertir: \n"))
    temperatura_a_convertir = float(input("Introduce la temperatura a convertir (solo unidades): \n"))
    if opcion_menu_t == 1:
        print(temperatura_a_convertir,"grados celsius es equivalente a",conversion_celsius(1,temperatura_a_convertir), "grados Farenheit")
    elif opcion_menu_t == 2:
        print(temperatura_a_convertir,"grados celsius es equivalente a",conversion_celsius(2,temperatura_a_convertir), "grados Kelvin")
    elif opcion_menu_t == 3:
        print(temperatura_a_convertir,"grados Farenheit es equivalente a",conversion_farenheit(1,temperatura_a_convertir), "grados Celsius")
    elif opcion_menu_t == 4:
        print(temperatura_a_convertir,"grados Farenheit es equivalente a",conversion_farenheit(2,temperatura_a_convertir), "grados Kelvin")
    elif opcion_menu_t == 5:
        print(temperatura_a_convertir,"grados Kelvin es equivalente a",conversion_kelvin(1,temperatura_a_convertir), "grados Celsius")
    elif opcion_menu_t == 6:
        print(temperatura_a_convertir,"grados Kelvin es equivalente a",conversion_kelvin(2,temperatura_a_convertir), "grados Farenheit")


def leer_tabla():
    root = 'C:/Users/garci/Desktop/Karen_calculadora/Tabla_periodica.txt'
    tabla = open(root, 'r')
    cant_elementos_tabla: int = 103
    str:  str = (input("Introduce el elemento a buscar: \n"))
    for i in range (cant_elementos_tabla):
        elemento_t = tabla.readline()
        tipo = elemento_t.split()
        if str == tipo[0]:
            print("Abreviatura:",tipo[0],"Nombre:", tipo[1],"Numero atomico",tipo[2],"Valencias",tipo[3],"Masa atomica",tipo[4])
            break


    tabla.close()


#Cargar variables de menu

m_molar: int = 1
ley_gas: int = 2
tabla_p: int = 3
conversion: int = 4
terminar: int = 5

print_menu_opciones()
opcion = int(input("Introduce la opcicion a escoger: \n"))

while True:
    if opcion == m_molar:
        print("Opcion masa molar")

    elif opcion == ley_gas:
        print("Opcion ley de gases")

    elif opcion == tabla_p:
        print("Opcion consultar tabla periodica")
        #elemento = str(input("Introduce la opcicion a escoger: \n"))
        leer_tabla()

    elif opcion == conversion:
        print("Opcion para conversion de temperatura")
        calcular_conversion_temp()
    elif opcion == terminar:
        break
    else:
        print("Seleccionar opcion valida")
    print_menu_opciones()
    opcion = int(input("Introduce la opcicion a escoger: \n"))

print("Fin de calculadora, Gracias ")




