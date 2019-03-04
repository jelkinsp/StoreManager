# -*- coding: utf-8 -*-
import model.movement as movement
import control.manager as manager


def get_date_movement():
    print("Introdece el codigo del almacen 2(PC)")
    c2 = input()
    print("Introdece la cantidad")
    quantity = input()

    return movement.Movement(c2, quantity)


manager.insert_movement(manager.create_connection(), get_date_movement())
