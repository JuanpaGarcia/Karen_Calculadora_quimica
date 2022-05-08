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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

#Cargar variables de menu

m_molar: int = 1
ley_gas: int = 2
tabla_p: int = 3
conversion: int = 4

print_menu_opciones()
opcion = int(input("Introduce la opcicion a escoger: \n"))

while opcion <= conversion:
    if opcion == m_molar:
        print("Opcion masa molar")

    elif opcion == ley_gas:
        print("Opcion ley de gases")

    elif opcion == tabla_p:
        print("Opcion consultar tabla periodica")

    elif opcion == conversion:
        print("Opcion para conversion de temperatura")
    else:
        print("Seleccionar opcion valida")
    print_menu_opciones()
    opcion = int(input("Introduce la opcicion a escoger: \n"))

print("Fin de calculadora ")




