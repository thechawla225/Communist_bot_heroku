import re
import requests
from flask import jsonify
import random
import os


def sample_responses(bot, text, chat_id):
    i = 100

    hello = ['hello olga', 'hello', 'hi', 'hey', 'hye']
    capitalists = ['biden', 'obama', 'america', 'trump', 'lincoln', 'canada']
    cuss_words = ['shit', 'fuck', 'fucking', 'shitting', 'shiting', 'cunt']
    cry = ["stalin is dead", "communism dosent work",
           "i hate communism", "communism sucks", "communism dosen't work"]
    our_words = ["we*", "ours*", "us*", "our*", "we", "our", "ours"]
    asks_name = ["what is your name?", "what is your name",
                 "what's your name?", "what's yout name", "whats your name?"]
    asks_meme = ["show us a meme", "show us a wewe", "show me a meme",
                 "show us a usus", "show us a meme", "can you share a meme?"]
    asks_status = ["how are you olga?", "how are you olga",
                   "how are you?", "how are u olga?", "how are u?", "how are u"]
    answer = ""

    switcher = {
        0: 'We do not talk about those Capitalists here, comrade ',
        1: answer,
        2: 'Comrade! there is no "I" in Communsm ',
        3: 'No need to thank me comrade, I serve the motherland',
        4: "Cyka Blyat!! That's not communist language!!",
        6: 'You make commie sad',
        7: "Let's start the revolution!! Share my username with 10 of your comrades, and let's make them OUR comrades",
        9: "I am Olga! your friendly neighbourhood communist!!",
        10: "Привет my comrade! Long live the revolution!",
        11: "Hello Comrade! I am Olga! your friendly neighbourhoob communist!"
    }

    if(text in asks_name):
        i = 9
        return switcher.get(i, "My Commie brain can't understand what you said comrade, I only understand communism")
    elif(text == "what can you do?"):
        return "To know what I can do, send /help"
    elif(text in cry):
        send_image(bot, chat_id, typeof="sad")
        i = 6
    elif(text == "how to start a revolution?"):
        i = 7
        send_audio(bot, chat_id)
        send_gif(bot, chat_id, typeof="revolution")
    elif(text in asks_meme):
        i = 8
        send_image(bot, chat_id, typeof="meme")
        return "Remember comrade, it's not a meme it's a wewe"
    if(text in asks_status):
        return "I'm just planning the next revolution comrade!"

    text = text.split(" ")
    text = [re.sub('[^a-zA-Z0-9]+', '', _) for _ in text]

    for txt in text:
        print(txt)
        if(txt in cuss_words):
            i = 4
            break
        elif(txt in capitalists):
            i = 0
            break
        elif(txt in hello):
            i = 10
        elif(txt in our_words):
            send_image(bot, chat_id, "happy")
            i = 5
            answer = txt
            return "Yes, " + answer
        elif(txt in ["meme"]):
            send_image(bot, chat_id, "meme")
            return "Remember comrade, it's not a meme it's a wewe"
        elif(txt == "me"):
            i = 1
            text = " ".join(text)
            answer = text.replace("me", "Us*")
            return answer
        elif(txt == "i"):
            i = 2
            break
        else:
            i = 100
    if(i == 100):
        send_gif(bot, chat_id, "random")

    return switcher.get(i, "My Commie brain can't understand what you said comrade, I only understand communism")


def send_image(bot, chat_id, typeof, image_name=None):
    meme_path = 'images/memes'

    sad = ['images/cries_in_soviet.jpg', 'images/sad_vodka_noises.jpg']
    happy = 'images/happy_stalin.jpg'
    if(typeof == "meme"):
        image_name = os.path.join(
            meme_path, str(random.randint(1, 22)) + '.jpg')
    elif(typeof == "sad"):
        image_name = random.choice(sad)
    elif(typeof == "happy"):
        image_name = happy

    bot.send_photo(chat_id, photo=open(image_name, 'rb'))


def send_gif(bot, chat_id, typeof=None, gif=None):
    random_gifs = [
        'https://tenor.com/view/communiste-communist-hugs-heart-red-gif-14360509',
        'https://tenor.com/view/comunismo-comunista-rojo-marx-stalin-gif-11647520',
        'https://tenor.com/view/capigifs-gomez-castro-communism-gif-13106558',
        'https://tenor.com/view/simpsons-lenin-crush-capitalism-funny-gif-5488019',
        'https://tenor.com/view/heart-love-mustache-change-color-gif-17567673',
        'https://tenor.com/view/communism-communist-stalin-gif-5148588',
        'https://tenor.com/view/marx-marxism-communism-intesifies-funny-gif-16697750',
        'https://tenor.com/view/carlos-marx-marx-karl-marx-gif-11822631',
        'https://tenor.com/view/communism-communist-dance-gif-5148596',
        'https://tenor.com/view/cccp-flag-wave-star-logo-gif-16196191',
        'https://tenor.com/view/ok-russia-communism-dance-country-gif-20317821'

    ]
    if(typeof == "random"):
        gif = random_gifs[random.randint(0, len(random_gifs)-1)]
    elif(typeof == "revolution"):
        gif = "https://tenor.com/view/elmo-gif-8869638"
    bot.sendDocument(chat_id, gif)


def send_audio(bot, chat_id):
    bot.send_audio(chat_id=chat_id, audio=open(
        'audios/sovietanthem.mp3', 'rb'))
