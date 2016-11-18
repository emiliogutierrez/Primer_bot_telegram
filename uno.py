#!/usr/bin/python
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler, CallbackQueryHandler

tokenid = "YOUR_TOKEN_ID"

def inl(bot, update):
    if update.callback_query.data == "k_light_on":
        #func for turn on light res = k_light.on()
        bot.answerCallbackQuery(callback_query_id=update.callback_query.id, text="Turning on light ON!")
        bot.editMessageText(inline_message_id=update.callback_query.inline_message_id, text="Do you want to turn On or Off light? Light is ON")
        #hardcoded vars variant
        #bot.editMessageText(message_id=298, chat_id=174554240, text="Do you want to turn On or Off light? Light is ON")
    elif update.callback_query.data == "k_light_off":
        #func for turn on light res = k_light.off()
        bot.answerCallbackQuery(callback_query_id=update.callback_query.id, text="Turning off light OFF!")
        bot.editMessageText(inline_message_id=update.callback_query.inline_message_id, text="Do you want to turn On or Off light? Light is ON")
        #hardcoded vars variant
        #bot.editMessageText(message_id=298, chat_id=174554240, text="Do you want to turn On or Off light? Light is OFF")
    else:
        print "Err"

def k_light_h(bot, update):
    reply_markup = telegram.InlineKeyboardMarkup([[telegram.InlineKeyboardButton("On", callback_data="k_light_on"), telegram.InlineKeyboardButton("Off", callback_data="k_light_off")]])
    ddd = bot.sendMessage(chat_id=update.message.chat_id, text="Do you want to turn On or Off light?", reply_markup=reply_markup)



if __name__ == "__main__":
    #
    updater = Updater(token=tokenid)
    ### Handler groups
    dispatcher = updater.dispatcher
    # light
    k_light_handler = CommandHandler('light', k_light_h)
    dispatcher.add_handler(k_light_handler)
    # errors
    updater.dispatcher.add_error_handler(error)
    updater.start_polling()
    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()
