def capturar():
    global lista
    lista = []
    n = int(input("cual es el rango de la lista: "))
    for i in range(0, n):
        print("ingrese el elemento: ",i)
        elemento = input()
        lista.insert(i, elemento)


def mostrar():
    print(lista)


def agregar():
    elemento = int(input("ingrese el valor nuevo: "))
    indice = int(input("ingrese el indice del valor nuevo: "))
    lista.insert(indice, elemento)
    print("nuevo elemento agregado")


def eliminar():
    indice = int(input("ingrese el indice del elemento que desea eliminar: "))
    del lista[indice]
    print("el elemento fue eliminado")


def menu_principal():
    opcion = "1"
    while opcion != 5:
        print("digite el numero de la opcion que desea realizar: ")
        print("1. capturar")
        print("2. mostrar")
        print("3. agregar")
        print("4. eliminar")
        print("5. salir")
        opcion = input()
        if opcion == "1":
            capturar()
        elif opcion == "2":
            mostrar()
        elif opcion == "3":
            agregar()
        elif opcion == "4":
            eliminar()

menu_principal()