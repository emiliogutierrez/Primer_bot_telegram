#!/usr/bin/python
# -*- coding: utf-8 -*-
# pip install python-telegram-bot
# pip show python-telegram-bot

import telebot # Librería de la API del bot.
from telebot import types # Tipos para la API del bot.
import time # Librería para hacer que el programa que controla el bot no se acabe.
import MySQLdb as mdb


TOKEN = '299056405:AAFv7EfClfn1M0VBe-xfD1YwXf9G2pLTfr4' # Nuestro tokken del bot (el que @BotFather nos dió).

pathx = "/home/emilio/repos/py/imagenesradar/"
bot = telebot.TeleBot(TOKEN) # Creamos el objeto de nuestro bot.


def listener(messages): # Con esto, estamos definiendo una función llamada 'listener', que recibe como parámetro un dato llamado 'messages'.
    for m in messages: # Por cada dato 'm' en el dato 'messages'
        cid = m.chat.id # Almacenaremos el ID de la conversación.
        # Establecemos la conexión con la base de datos
        con = mdb.connect("localhost","root","15571613","triviaEA")
        cur = con.cursor()
        cur.execute("SELECT * FROM trivia")
        for i in range(cur.rowcount):
            row = cur.fetchone()
            op1 = row[6]
            op2 = row[7]
            op3 = row[8]
            op4 = row[9]



        markup = types.ReplyKeyboardMarkup(row_width=1)
        itembtn1 = types.KeyboardButton(op1)
        itembtn2 = types.KeyboardButton(op2)
        itembtn3 = types.KeyboardButton(op3)
        itembtn4 = types.KeyboardButton(op4)

        markup.add(itembtn1, itembtn2, itembtn3,itembtn4)
        bot.send_message(cid, "Selecciona una imagen", reply_markup=markup)

        # or add KeyboardButton one row at a time:
#        markup = types.ReplyKeyboardMarkup()
#        itembtna = types.KeyboardButton('a')
#        itembtnv = types.KeyboardButton('v')
#        itembtnc = types.KeyboardButton('c')
#        itembtnd = types.KeyboardButton('d')
#        itembtne = types.KeyboardButton('e')
#        markup.row(itembtna, itembtnv)
#        markup.row(itembtnc, itembtnd, itembtne)
#        bot.send_message(cid, "Choose one letter:", reply_markup=markup)
        if m.content_type == 'text': # Filtramos mensajes que sean tipo texto.
            archi=open(pathx+'ultimaactualizacion.txt','r')
            linea=archi.readline()
            while linea!="":
                actu=linea
                linea=archi.readline()
            archi.close()
            zona = ""
            mensaje = str(m.chat.first_name) + ': Te envio imagen de Radar, actulizada al ' + str(actu)
            if m.text == 'Imagen Radar Sur':
                zona = 'Sur'
                photo = open(pathx+'sur.gif', 'rb')
                bot.send_message(cid, mensaje) # Ejemplo tb.send_message('109556849', 'Hola mundo!')
                bot.send_photo(cid, photo)
            elif m.text == 'Imagen Radar Centro':
                zona = 'Centro'
                photo = open(pathx+'centro.gif', 'rb')
                bot.send_message(cid,  str(m.chat.first_name) + ': Te envio imagen de Radar actulizada al ' + str(actu)     ) # Ejemplo tb.send_message('109556849', 'Hola mundo!')
                bot.send_photo(cid, photo)
            elif m.text == 'Imagen Radar Norte':
                zona = 'Norte'
                photo = open(pathx + 'norte.gif', 'rb')
                bot.send_message(cid,  str(m.chat.first_name) + ': Te envio imagen de Radar actulizada al ' + str(actu)   ) # Ejemplo tb.send_message('109556849', 'Hola mundo!')
    #            bot.send_photo(cid, photo)
            elif m.text == 'Animacion Radar General':
                zona = 'Animacion'
                photo = open(pathx+ 'animacion.gif', 'rb')
                bot.send_message(cid,  str(m.chat.first_name) + ': En face de prueba no enviamos la animacion porque es un archivo muy grande, intenta con las otras opciones, disculpa las molestias ' + str(actu)   ) # Ejemplo tb.send_message('109556849', 'Hola mundo!')
                bot.send_photo(cid, photo)
            elif m.text == 'Imagen Radar General':
                zona = 'General'
                photo = open(pathx+ 'latest.gif', 'rb')
                bot.send_message(cid,  str(m.chat.first_name) + ': Te envio imagen de Radar actulizada al ' + str(actu)   ) # Ejemplo tb.send_message('109556849', 'Hola mundo!')
                bot.send_photo(cid, photo)
        elif m.content_type != 'text':
            bot.send_message(cid,  str(m.chat.first_name) + ' opcion no valida ' ) # Ejemplo tb.send_message('109556849', 'Hola mundo!')



        #    elif  m.text !=  '/s' or m.text !=  '/c' or m.text !=  '/n' or  m.text !=  '/c' or m.text !=  '/g' or m.text !=  '/a':
        #        zona =  "  OPCION INVALIDA "
        #        mensaje = "--> " + str(m.text) + " <--" + " no es un opcion valida.-"
        #        bot.send_message(cid,  str(m.chat.first_name) + ": " +  mensaje   ) # Ejemplo tb.send_message('109556849', 'Hola mundo!')
        #    elif m.content_type == "location":
        #        print str(m.location.latitude) + "   --   " + str(m.location.longitude) + str(m.chat.first_name)
# tb.send_location(chat_id, latitud, longitud)
# Envia la imagen a quien la pide
        # print "[" + str(cid) + "]: Escribio : " +  m.text + " Envia imagen " + str(zona) +  " a :" + str(m.chat.first_name) + " --  " + str(actu)
#        print "[" + str(cid) + "]:  Imagen: " + str(zona) +  " -- Nombre: " + str(m.chat.first_name) + " " +str(m.chat.last_name) + " -- Fecha/Hora: "+ str(actu)  + "---" + str(m.text)
        print "[" + str(cid) + "]:"  + " -- Nombre: " + str(m.chat.first_name) + " -- " + str(m.chat.last_name) + "  Zona " + str(zona)

bot.set_update_listener(listener) # Así, le decimos al bot que utilice como función escuchadora nuestra función 'listener' declarada arriba.

bot.polling(none_stop=True) # Con esto, le decimos al bot que siga funcionando incluso si encuentra algún fall
