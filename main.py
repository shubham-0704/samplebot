import Constants as keys
from telegram.ext import * 
import Responses as R

print("bot started")

def start_command(update,context):
    update.message.reply_text('Type something')

def help_command(update,context):
    update.message.reply_text('search on google')

def handle_message(update,context):
    text= str(update.message.text).lower()
    respone =R.resp(text)

    update.message.reply_text(respone)

def error(update ,context):
    print(f"Update {update} cuse error {context.error}")

def main():
    updater =Updater(keys.Apikey,use_context=True)

    dp= updater.dispatcher
    dp.add_handler(CommandHandler("start",start_command))
    dp.add_handler(CommandHandler("help",help_command))
    dp.add_handler(MessageHandler(Filters.text,handle_message))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()
    
main()