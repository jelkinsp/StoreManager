# -*- coding: utf-8 -*-
import mysql.connector as mysql


def connection_db():
    data_base = mysql.connect(
        host="localhost",
        database="almacen_sge",
        user="root",
        password="")

    return data_base
