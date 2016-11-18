#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
import MySQLdb as mdb

# Establecemos la conexión con la base de datos
con = mdb.connect("localhost","root","15571613","triviaEA")



with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM trivia")
    for i in range(cur.rowcount):
        row = cur.fetchone()
        
        print row[6]
