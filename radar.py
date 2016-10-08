import telebot # Importamos las librería

TOKEN = '<token string>' # Ponemos nuestro Token generado con el @BotFather

tb = telebot.TeleBot(TOKEN) # Combinamos la declaración del Token con la función de la API


tb.send_message(chatid, text) # Ejemplo tb.send_message('109556849', 'Hola mundo!')

# Enviar una simple foto
#  photo = open('/home/lordsergio/Gatito_Feliz.jpg', 'rb')
#  tb.send_photo(chat_id, photo)

doc = open('/home/lordsergio/Documentos/deberes_de_verano.pdf', 'rb') # Es la función equivalente a enviar un archivo desde telegram.
tb.send_document(chat_id, doc)

tb.send_message(109556849, 'Disfruta de tu verano ;)')
