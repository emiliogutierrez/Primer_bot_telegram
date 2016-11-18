#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
This Example will show you how to use register_next_step handler.
"""
import time
import telebot
from telebot import types
import MySQLdb as mdb
from random import shuffle


API_TOKEN = '261381855:AAFCaB8qKhvKAqNMRUtC2AQUo7eqxt2ts10'

bot = telebot.TeleBot(API_TOKEN)

user_dict = {}


class User:
    def __init__(self, name):
        self.name = name
        self.age = None
        self.sex = None


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start', 'jugar', 'j','play'])
#def send_welcome(message):

#    msg = bot.reply_to(message, """\
#Hola, este es una trivia de la EA .
#""")
#    bot.register_next_step_handler(msg, process_central)


def process_central(message):
#    print "procesoscentral"
    try:
        chat_id = message.chat.id
#-------------------------------------------
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('A','B','C','D')
        pregunta, respuesta1, respuesta2,respuesta3,respuesta4 = conectaDB(chat_id)
        global respuesta_correcta
        respuesta_correcta = 'Z'
        mensaje, respuesta_correcta = armaPregunta(respuesta1, respuesta2, respuesta3, respuesta4, pregunta, chat_id)
        bot.send_message(chat_id, mensaje , reply_markup=markup)
#-----------------------------------------
        name = message.text
        user = User(name)
        user_dict[chat_id] = user
#        msg = bot.reply_to(message, 'How old are you?')
        bot.register_next_step_handler(message, process_analiza_respueta)
    except Exception as e:
        bot.reply_to(message, 'oooops a ocurrido un error !')
#--------------------------------------
def process_analiza_respueta(message):
#    print message.text[1]
    try:
        if respuesta_correcta == message.text:
            markupx = types.ForceReply(selective=False)
#            print message.chat.id
            bot.send_message(message.chat.id, 'CAPOOOOOOOOO')
#            bot.register_next_step_handler(message, process_central)
            process_central()
            return
        elif respuesta_correcta != message.text:
            msg = bot.reply_to(message, ' no es la correcta sigue estudiando ')
            process_central()
#            bot.register_next_step_handler(message, process_central)
            return
    except Exception as e:
        bot.reply_to(message, 'Que pasoooo oooops')
#--------------------------------------------------------------------
def process_sex_step(message):
    try:
        chat_id = message.chat.id
        sex = message.text
        user = user_dict[chat_id]
        if (sex == u'Male') or (sex == u'Female'):
            user.sex = sex
        else:
            raise Exception()
        bot.send_message(chat_id, 'Nice to meet you ' + user.name + '\n Age:' + str(user.age) + '\n Sex:' + user.sex)
    except Exception as e:
        bot.reply_to(message, 'oooops')


def conectaDB(cid):
# Establecemos la conexión con la base de datos
    con = mdb.connect("localhost","root","15571613","triviaEA")
    x = con.cursor()
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
            respuesta_correcta = arreglo[i][1]
#            print arreglo[i][1] , "En el llamado a Funcion  ", respuesta_correcta
            break
    mensaje = "😊 " + pregunta +  "?" + "\n\n" + arreglo[0] + "\n"  + arreglo[1] + "\n"  + arreglo[2] + "\n" + arreglo[3] + "\n"

#    print mensaje, "###  ",  respuesta_correcta
    return mensaje, respuesta_correcta

# bot.set_update_listener(process_central)
bot.polling()
