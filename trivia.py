#!/usr/bin/python
# -*- coding: utf-8 -*-
# pip install python-telegram-bot
# pip show python-telegram-bot

import telebot # Librería de la API del bot.
from telebot import types # Tipos para la API del bot.
import time # Librería para hacer que el programa que controla el bot no se acabe.
import MySQLdb as mdb
from random import shuffle

TOKEN = '261381855:AAFCaB8qKhvKAqNMRUtC2AQUo7eqxt2ts10' # Nuestro tokken del bot (el que @BotFather nos dió).
pathx = "/home/emilio/repos/py/imagenesradar/"
bot = telebot.TeleBot(TOKEN) # Creamos el objeto de nuestro bot.

def listener(messages): # Con esto, estamos definiendo una función llamada 'listener', que recibe como parámetro un dato llamado 'messages'.
    for m in messages: # Por cada dato 'm' en el dato 'messages'
        cid = m.chat.id # Almacenaremos el ID de la conversación.
        # Establecemos la conexión con la base de datos
        if m.content_type == 'text': # Filtramos mensajes que sean tipo texto.
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
#                markup = types.ReplyKeyboardMarkup(row_width=2, force_reply)
            markup.add('A','B','C','D')
            pregunta, respuesta1, respuesta2,respuesta3,respuesta4 = conectaDB(cid)
            resputacorrecta, mensaje = armaPregunta(respuesta1, respuesta2, respuesta3, respuesta4, pregunta, cid)
            bot.send_message(cid, mensaje , reply_markup=markup)
            #    bot.send_message("212880702", "------ ")
            print "antes de enviar mensaje", m.text
#               bot.send_message(cid, mensaje  , reply_markup=markup)
            print "despues de enviar mensaje", m.text
            respuestacorrecta1 = '/'+resputacorrecta
#                print resputacorrecta, "<------>" ,respuestacorrecta1, "----->", m.text , " --- "
            if m.text != resputacorrecta:
                mensaje = "Ummm sigue practicando " + "La correcta " + resputacorrecta
                bot.send_message(cid, mensaje) # Ejemplo tb.send_message('109556849', 'Hola mundo!')
            elif m.text == resputacorrecta:
                mensaje = "Bien AHIII !!! "
                bot.send_message(cid, mensaje) # Ejemplo tb.send_message('109556849', 'Hola mundo!')
        elif m.content_type != 'text':
            bot.send_message(cid,  str(m.chat.first_name) + ' opcion no valida ' ) # Ejemplo tb.send_message('109556849', 'Hola mundo!')
#        print "[" + str(cid) + "]:"  + " -- Nombre: " + str(m.chat.first_name) + "," + str(m.chat.last_name) + " --- " + m.text
#--------------------------------------------------------------------------
def conectaDB(cid):
# Establecemos la conexión con la base de datos
    con = mdb.connect("localhost","root","15571613","triviaEA")
    x = con.cursor()
#    INSERT INTO `Conexiones` (`id`, `chat_id`, `ctime`) VALUES (NULL, cid, CURRENT_TIMESTAMP)
#    try:
#    x.execute('select max(id) from Conexiones')
#    row = x.fetchone()
#    idnuevoregistro = row[0]+1
    idnuevoregistro = None
    query = "INSERT INTO Conexiones(id,chat_id) " \
            "VALUES(%s,%s)"
    args = (idnuevoregistro, cid)
    try:
        x.execute(query, args)
        con.commit()
    except:
        con.rollback()
#    conn.close()
    try:
        cur = con.cursor()
        cur.execute("SELECT * FROM Preguntas")
        row = cur.fetchone()
        return row[6], row[7], row[8], row[9], row[10]
    except:
        con.rollback()
#--------------------------------------------------------------------
def armaPregunta(respuesta1, respuesta2, respuesta3, respuesta4, pregunta, cid):
    respuesta1 = respuesta1 + "-OKOKOK-"
    arreglo = [respuesta1, respuesta2, respuesta3, respuesta4 ]
    shuffle(arreglo)
    x=0
    arreglo[x]  = "/A " + str(arreglo[x])
    x += 1
    arreglo[x]  = "/B " + str(arreglo[x])
    x += 1
    arreglo[x]  = "/C " + str(arreglo[x])
    x += 1
    arreglo[x]  = "/D " + str(arreglo[x])
    for i in range(0,4):
        if arreglo[i].find('-OKOKOK-') != -1:
            arreglo[i] = arreglo[i].replace('-OKOKOK-','')
            lacorrectaes = arreglo[i][1]
            break
    mensaje = "😊 " + pregunta +  "?" + "\n\n" + arreglo[0] + "\n"  + arreglo[1] + "\n"  + arreglo[2] + "\n" + arreglo[3]
    print mensaje
    return lacorrectaes, mensaje
#--------------------------------------------------------------------

# bot.notifyOnMessage(listener)
bot.set_update_listener(listener) # Así, le decimos al bot que utilice como función escuchadora nuestra función 'listener' declarada arriba.
bot.polling(none_stop=True) # Con esto, le decimos al bot que siga funcionando incluso si encuentra algún fall

while 1:
    time.sleep(10)
