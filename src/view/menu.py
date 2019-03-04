# -*- coding: utf-8 -*-
import src.model.movement as movement
import src.model.storage as storage
import src.model.reference as reference
import src.control.manager as manager

"""Gestor del Menu
Controla todas las entradas por teclado y las salidas por consola

"""


def start_menu():
    """Crear el menu princial
    Crea el menu principal, estara pidiendo opciones hasta que elija la opcion de salir
    """
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
            manager.query_store_items1(manager.create_connection())
        elif selection == "2":
            print("---- Mostrar almacen 2 ----")
            manager.query_store_items2(manager.create_connection())
        elif selection == "3":
            print("---- Mostrar movimiento ----")
            manager.query_movement(manager.create_connection())
        elif selection == "4":
            print("---- Mostrar tabla de referencias ----")
            manager.query_reference_table(manager.create_connection())
        elif selection == "5":
            print("---- Añadir un movimiento ----")
            manager.insert_movement(manager.create_connection(), get_input_movement())
        elif selection == "6":
            print("---- Añadir componentes al almacen 1 ----")
            manager.insert_store_item1(manager.create_connection(), get_input_store())
        elif selection == "7":
            print("---- Añadir productos al almacen 2 ----")
            manager.insert_store_item2(manager.create_connection(), get_input_store())
        elif selection == "8":
            print("---- Añadir referencia ----")
            manager.insert_referenece(manager.create_connection(), get_input_reference())
        elif selection == "9":
            print("---- Eliminar movimiento ----")
            manager.delete_movement(manager.create_connection(), delete_input_movement())
        elif selection == "10":
            print("---- Eliminar referencia ----")
            manager.delete_reference(manager.create_connection(), get_input_reference())
        elif selection == "11":
            print("---- Eliminar componentes al almacen 1 ----")
            manager.delete_store_item1(manager.create_connection(), delete_input_storage())
        elif selection == "12":
            print("---- Elminar productos al almacen 2 ----")
            manager.delete_store_item2(manager.create_connection(), delete_input_storage())
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


def get_input_store():
    print("Introdece el codigo del almacen")
    code = input()
    # code = "B0003"
    print("Introdece la cantidad")
    quantity = input()
    # quantity = 3
    print("Introdece la descripcion")
    description = input()
    # description = "TEST"

    return storage.Storage(code, quantity, description)


def delete_input_storage():
    print("Introdece el codigo del almacen que queires eliminar")
    code = input()
    # code = "B0003"
    return storage.Storage(code, 0, "")


def get_input_reference():
    print("Introdece el codigo del productor del almacen 2(PC)")
    c2 = input()
    # c2 = "B0003"
    loop = True
    c1 = list()
    while loop:
        print("Introdece el codigo del productor del almacen 1(Componentes)")
        c1.append(input())
        if input("Quieres añadir otro?(y/n)") == "n":
            loop = False
    # c1 = "B0003"
    print("Introdece la cantidad")
    quantity = input()
    # quantity = 3

    return reference.Reference(c2, c1, quantity)


def delete_input_reference():
    print("Introdece el codigo del productor del almacen 2(PC)")
    c2 = input()
    # c2 = "B0003"
    return reference.Reference(c2, 0, 0)
