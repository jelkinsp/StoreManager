# -*- coding: utf-8 -*-
import control.connection as connect

""" Gestion de la base de datos
Todas las consultas y modificaciones se realizan aqui.

Example:
    Ejemplo de consulta a la base de datos::
    
        $ query_store_items2(create_connection())

Esto devuelve todo los datos almacenados en el almacen 2 

Todo:
    * Invertir movimiento
    * Insertar productos en el almacen 2
    * Insertar componentes en el almacen 1
    * Insertar referencias de las 2 insercciones anteriores

"""


def create_connection():
    """Crear la conexion 
    Crea una conexion a la base de datos
    Returns:
        Retorna la conexion a la base de datos
    """
    return connect.connection_db()


def query_store_items1(data_base):
    """Consultar al almacen1 todos los datos
    Consulta los datos y los devuelve en forma lista los datos    
    Attributes:
        data_base (mysql): Conexion a la base de datos
    Returns:
        Retorna una lista con los datos del almacen1
    """
    cursor = data_base.cursor()
    cursor.execute("SELECT * FROM storage1")
    result_set = list(cursor.fetchall())
    for item in result_set:
        print(item)

    data_base.close()

    return result_set


def query_store_items2(data_base):
    """Consultar al almacen2 todos los datos
    Consulta los datos y los devuelve en forma lista los datos    
    Attributes:
        data_base (mysql): Conexion a la base de datos
    Returns:
        Retorna una lista con los datos del almacen2
    """
    cursor = data_base.cursor()
    cursor.execute("SELECT * FROM storage2")
    result_set = list(cursor.fetchall())
    for item in result_set:
        print(item)

    data_base.close()

    return result_set


def query_store_items1_code(data_base, code):
    """Consultar el almacen1 por el codigo
    Consulta los datos y los devuelve en forma lista los datos    
    Attributes:
        data_base (mysql): Conexion a la base de datos
        code (int): Codigo de la tabla
    Returns:
        Retorna una lista con los datos del almacen1
    """
    cursor = data_base.cursor()
    cursor.execute("SELECT * FROM storage1 WHERE code=%s", code)
    result_set = list(cursor.fetchall())
    for item in result_set:
        print(item)

    data_base.close()

    return result_set


def query_store_items2_code(data_base, code):
    """Consultar el almacen2 por el codigo
    Consulta los datos y los devuelve en forma lista los datos    
    Attributes:
        data_base (mysql): Conexion a la base de datos
        code (int): Codigo de la tabla
    Returns:
        Retorna una lista con los datos del almacen2
    """
    cursor = data_base.cursor()
    cursor.execute("SELECT * FROM storage2 WHERE code=%s", code)
    result_set = list(cursor.fetchall())
    for item in result_set:
        print(item)

    data_base.close()

    return result_set


def query_reference_table_code(data_base, c2):
    """Consultar tabla de referencias por el c2
    Consulta los datos y los devuelve en forma lista los datos    
    Attributes:
        data_base (mysql): Conexion a la base de datos
        c2 (int): codigo del almacen2
    Returns:
        Retorna una lista con los datos de la la table de referencias
    """
    cursor = data_base.cursor()
    cursor.execute("SELECT C1, quantity FROM reference_table WHERE C2=%s", (c2,))
    result_set = list(cursor.fetchall())
    # for item in result_set:
    #     print(item)
    return result_set


def insert_movement(data_base, movement):
    """Inserccion de un movimiento
    Inserta un movimiento a la tabla, modifica la tabla del almacen 2 para sumanle la cantidad adquirida y
    modifica la tabla del almacen 1 para restarles los datos que se requieren en la construcion del producto
    
    Attributes:
        data_base (mysql): Conexion a la base de datos
        movement (Movement): Objeto que contiene los datos de la inserccion
    """
    cursor = data_base.cursor()
    cursor.execute("INSERT INTO movement VALUES(null,SYSDATE(),%s,%s)", (movement.c2, movement.quantity))
    cursor = data_base.cursor()
    cursor.execute("UPDATE storage2 SET code=%s, quantity=quantity+%s WHERE code=%s",
                   (movement.c2, movement.quantity, movement.c2))
    referece_list = query_reference_table_code(data_base, movement.c2)
    for i in range(movement.quantity):
        for reference in referece_list:
            cursor = data_base.cursor()
            cursor.execute("UPDATE storage1 SET quantity=quantity-%s WHERE code=%s",
                           (str(reference[1]), reference[0]))
    data_base.commit()
    data_base.close()
