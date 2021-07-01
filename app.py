from flask import Flask, request
from telegram.ext import *
import responses as R
import telegram
from telegram import *
import time

app = Flask(__name__)

global bot
global TOKEN
TOKEN = "1873676859:AAFB8UY732ubRu38lcQzbvqMQRncPDLexOg"
URL = "Heroku link to be created later"

bot = telegram.Bot("1873676859:AAFB8UY732ubRu38lcQzbvqMQRncPDLexOg")
banhammer_gif = "https://tenor.com/JZWk.gif"
communism_intensifies_gif = 'https://tenor.com/view/marx-marxism-communism-intesifies-funny-gif-16697750'
print("The Revolution has began")


def start(update, context):
    update.message.reply_text(
        'The Revolution has began comrade use /help to see what I can do')


def help_command(update, context):
    update.message.reply_text('Hello Comrade! You can say things similar to : 1. "show me a meme" 2. "what do you think about Biden?" 3. say curse words like "fuck" 4. ask me how I am and many more things! contribute to my code by going to my description , more coming soon ')


def getAdminIDs(update):
    admins = bot.getChatAdministrators(update.message.chat_id)
    IDs = []
    for admin in admins:
        IDs.append(admin.user.id)
    return IDs


def banHammer(update, context):
    message = update.message
    sender = message.from_user.id
    IDs = getAdminIDs(update)
    if(sender in IDs):
        try:
            reciever = message.reply_to_message.from_user.id
            try:
                chatId = update.message.chat.id
                bot.restrictChatMember(
                    chatId, reciever, ChatPermissions(can_send_messages=False))
                update.message.reply_text(
                    "Comrade will be muted for 15 seconds")
                send_gif(chatId, banhammer_gif)
                time.sleep(15)
                bot.restrictChatMember(
                    chatId, reciever, ChatPermissions(can_send_messages=True))
            except:
                update.message.reply_text(
                    "Sorry Comrade! I can't mute a commander!")
        except:
            update.message.reply_text(
                "Who should I mute commander?")
    else:
        update.message.reply_text(
            "Cyka Blyat!! become a commander first!!")


def handle_message(update, context):
    text = str(update.message.text).lower()
    if(update.message.chat.type != "supergroup" and update.message.chat.type != "group"):
        chatid = update.message.chat_id
        message = update.message
        response = R.sample_responses(bot, text, chatid)
        update.message.reply_text(response)
    elif("olga" in text):
        update.message.reply_text("I've been mentioned!")


def send_gif(chat_id, document=communism_intensifies_gif):
    bot.sendDocument(chat_id, document)


def error(update, context):
    print(f"Update {update} caused error {context.error}")


@app.route('/setwebhook', methods=['GET', 'POST'])
def set_webhook():
    s = bot.setWebhook('{URL}{HOOK}'.format(URL=URL, HOOK=TOKEN))
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"


@app.route('/')
def index():
    return '.'


def main():
    print("main called")
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("banhammer", banHammer))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    app.run(threaded=True)
