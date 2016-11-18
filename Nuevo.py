#!/usr/bin/python
# -*- coding: utf-8 -*-

# Enviar nro de telefono
#
#
#
import telebot # Librería de la API del bot.
# from telebot import types # Tipos para la API del bot.
import time # Librería para hacer que el programa que controla el bot no se acabe.
import json

TOKEN = '299056405:AAFv7EfClfn1M0VBe-xfD1YwXf9G2pLTfr4' # Nuestro tokken del bot (el que @BotFather nos dió).

bot = telebot.TeleBot(TOKEN) # Creamos el objeto de nuestro bot.

def listener(messages): # Con esto, estamos definiendo una función llamada 'listener', que recibe como parámetro un dato llamado 'messages'.
    for m in messages: # Por cada dato 'm' en el dato 'messages'
        if m.content_type == 'text': # Filtramos mensajes que sean tipo texto.
            cid = m.chat.id # Almacenaremos el ID de la conversación.
            archi=open('/home/emilio/repos/py/imagenesradar/ultimaactualizacion.txt','r')
            linea=archi.readline()
            while linea!="":
                actu=linea
                linea=archi.readline()
            archi.close()
            zona = ""
            mensaje = str(m.chat.first_name) + ': Te envio imagen de Radar, actulizada al ' + str(actu)
#            teclado = []
#            row1 = ["card1", "card2", "card3"]
#            teclado.append(row1)
#            print "---"
#            print teclado
#            print "---"
#            reply_markup = {'keyboard': [['1'],['2']], 'resize_keyboard': True, 'one_time_keyboard': True}
            # bot.send_message(chat_id=cid, text="Ejemplo", reply_markup=reply_markup)
            if m.text == '/s':
                zona = 'Sur'
                photo = open('/home/emilio/repos/py/imagenesradar/sur.gif', 'rb')
                bot.send_message(cid, mensaje    ) # Ejemplo tb.send_message('109556849', 'Hola mundo!')
                bot.send_photo(cid, photo)
            elif m.text == '/c':
                zona = 'Centro'
                photo = open('/home/emilio/repos/py/imagenesradar/centro.gif', 'rb')
                bot.send_message(cid,  str(m.chat.first_name) + ': Te envio imagen de Radar actulizada al ' + str(actu)     ) # Ejemplo tb.send_message('109556849', 'Hola mundo!')
                bot.send_photo(cid, photo)
            elif m.text == '/n':
                zona = 'Norte'
                photo = open('/home/emilio/repos/py/imagenesradar/norte.gif', 'rb')
                bot.send_message(cid,  str(m.chat.first_name) + ': Te envio imagen de Radar actulizada al ' + str(actu)   ) # Ejemplo tb.send_message('109556849', 'Hola mundo!')
                bot.send_photo(cid, photo)
            elif m.text == '/a':
                zona = 'Animacion '
#                photo = open('/home/emilio/repos/py/imagenesradar/animacion.gif', 'rb')
                bot.send_message(cid,  str(m.chat.first_name) + ': En face de prueba no enviamos la animacion porque es un archivo muy grande, intenta con las otras opciones, disculpa las molestias ' + str(actu)   ) # Ejemplo tb.send_message('109556849', 'Hola mundo!')
#                bot.send_photo(cid, photo)
            elif m.text == '/g':
                zona = 'General'
                photo = open('/home/emilio/repos/py/imagenesradar/latest.gif', 'rb')
                bot.send_message(cid,  str(m.chat.first_name) + ': Te envio imagen de Radar actulizada al ' + str(actu)   ) # Ejemplo tb.send_message('109556849', 'Hola mundo!')
                bot.send_photo(cid, photo)
            elif m.text !=  '/s' or m.text !=  '/c' or m.text !=  '/n' or  m.text !=  '/c' or m.text !=  '/g' or m.text !=  '/a':
                zona =  " ERRORRRRRRR "
#                mensaje = "--> " + str(m.text) + " <--" + " no es un opcion valida.-"
                bot.send_message(cid,  str(m.chat.first_name) + ": " +  mensaje   ) # Ejemplo tb.send_message('109556849', 'Hola mundo!')



#             bot.sendMessage(chat_id= dd.get("chatid", None), text="/", reply_markup=repl)

# Envia la imagen a quien la pide

#    print "[" + str(cid) + "]: Escribio : " +  m.text + " Envia imagen " + str(zona) +  " a :" + str(m.chat.first_name) + " --  " + str(actu)
    print "[" + str(cid) + "]:  Imagen: " + str(zona) +  " -- Nombre: " + str(m.chat.first_name) + " -- Fecha/Hora: "+ str(actu)



bot.set_update_listener(listener) # Así, le decimos al bot que utilice como función escuchadora nuestra función 'listener' declarada arriba.
bot.polling(none_stop=True) # Con esto, le decimos al bot que siga funcionando incluso si encuentra algún fallo.
