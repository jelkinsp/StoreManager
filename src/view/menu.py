# -*- coding: utf-8 -*-
import src.model.movement as movement
import src.control.manager as manager


def start_menu():
    print("----Gestor de Base de datos en Python----")
    loop = True
    while loop:
        selection = input("""Seleccione una opcion
        1- Mostrar almacen 1
        2- Mostrar almacen 2
        3- Mostrar movimiento
        4- Mostrar tabla de referencias
        5- Añadir un movimiento
        6- Añadir componentes al almacen 1
        7- Añadir productos al almacen 2
        8- Añadir referencia
        9- Eliminar movimiento
        10- Eliminar referencia
        11- Eliminar componentes al almacen 1
        12- Elminar productos al almacen 2
        13- Salir
        """)
        if selection == "1":
            print("---- Mostrar almacen 1 ----")
        elif selection == "2":
            print("---- Mostrar almacen 2 ----")
        elif selection == "3":
            print("---- Mostrar movimiento ----")
        elif selection == "4":
            print("---- Mostrar tabla de referencias ----")
        elif selection == "5":
            print("---- Añadir un movimiento ----")
            manager.insert_movement(manager.create_connection(), get_input_movement())
        elif selection == "6":
            print("---- Añadir componentes al almacen 1 ----")
        elif selection == "7":
            print("---- Añadir productos al almacen 2 ----")
        elif selection == "8":
            print("---- Añadir referencia ----")
        elif selection == "9":
            print("---- Eliminar movimiento ----")
            manager.delete_movement(manager.create_connection(), delete_input_movement())
        elif selection == "10":
            print("---- Eliminar referencia ----")
        elif selection == "11":
            print("---- Eliminar componentes al almacen 1 ----")
        elif selection == "12":
            print("---- Elminar productos al almacen 2 ----")
        elif selection == "13":
            print("Saliendo del programa...")
            loop = False
        else:
            print("Has selecionado una opcion no disponible")


def get_input_movement():
    print("Introdece el codigo del productor del almacen 2(PC)")
    c2 = input()
    # c2 = "B0003"
    print("Introdece la cantidad")
    quantity = input()
    # quantity = 3

    return movement.Movement(c2, quantity)


def delete_input_movement():
    print("Introdece el codigo del productor del almacen 2(PC)")
    c2 = input()
    # c2 = "B0003"
    return movement.Movement(c2, 0)
