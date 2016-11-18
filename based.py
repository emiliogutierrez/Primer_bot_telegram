#!/usr/bin/python
# -*- coding: utf-8 -*-



import MySQLdb

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASS = '15571613'
DB_NAME = 'triviaEA'
print "1"
def run_query(query=''):
    datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME]
    print 2
    conn = MySQLdb.connect(*datos) # Conectar a la base de datos
    cursor = conn.cursor()         # Crear un cursor
    cursor.execute(query)          # Ejecutar una consulta

    if query.upper().startswith('SELECT * from trivia'):
        data = cursor.fetchall()   # Traer los resultados de un select
    else:
        conn.commit()              # Hacer efectiva la escritura de datos
        data = None

    cursor.close()                 # Cerrar el cursor
    conn.close()                   # Cerrar la conexión

    return data
