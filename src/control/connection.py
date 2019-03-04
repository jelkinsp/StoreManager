# -*- coding: utf-8 -*-
import mysql.connector as mysql

"""Conexion a la base de datos

Crean una conexion a la base de datos


Example:
    Ejemplo de creacion::
    
        $ import model.connection as connect
        $ cursor = connect.connection_db()
        
Author: Jose Luis Luengo Ramos

"""


def connection_db():
    data_base = mysql.connect(
        host="localhost",
        database="stores_db",
        user="root",
        password="")
    return data_base
