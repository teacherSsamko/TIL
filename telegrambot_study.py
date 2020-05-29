import telegram
from telegram.ext import Updater

demo_token = '810126667:AAEsaMlk8fS2NNSMcFWjuzc_p4Q8nrv2UkA'

demo_bot = telegram.Bot(token=demo_token)


def echo(bot, update):
    demo_bot.sendMessage(chat_id=update.message.chat_id,
                         text=update.message.text)


demo_room = '654244637'

msg = '테스트'

demo_bot.sendMessage(chat_id=demo_room, text=msg)
