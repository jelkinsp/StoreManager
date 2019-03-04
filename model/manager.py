# -*- coding: utf-8 -*-
import control.connection as connect


def create_connection():
    return connect.connection_db()


def query_store_items1(data_base):
    cursor = data_base.cursor()
    cursor.execute("SELECT * FROM almacen1")
    result_set = list(cursor.fetchall())
    for item in result_set:
        print(item)

    data_base.close()

    return result_set


def query_store_items2(data_base):
    cursor = data_base.cursor()
    cursor.execute("SELECT * FROM almacen2")
    result_set = list(cursor.fetchall())
    for item in result_set:
        print(item)

    data_base.close()

    return result_set


def insert_movement(data_base):
    cursor = data_base.cursor()
    cursor.execute("INSERT INTO ")
