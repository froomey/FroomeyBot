#-*- coding: utf-8 -*-
import telebot
import constantsss
import dialogs
import os
import random
from flood_meter import FloodMeter


bot = telebot.TeleBot(constantsss.token)
flood_meter = FloodMeter()


@bot.message_handler(content_types=["text"])
def reply(message):

    flood_meter.check_message()

    commands = {
        u", а?" : (bot.send_message, "хуй на"),
        u"триста" : (bot.reply_to, message, random.choice(dialogs.trista)),
        u"300" : (bot.reply_to, message, random.choice(dialogs.trista)),
        u"Тракторист сегодня я, отсоси ты у меня" : (bot.reply_to, message, random.choice(dialogs.trista2)),
        u"Годен я, сомнений нет, лучше сделай мне минет" : (bot.reply_to, message, random.choice(dialogs.trista3)),
        u"тракторист" : (bot.reply_to, message, random.choice(dialogs.)),
		u"Ну!" : (bot.reply_to, message, random.choice(dialogs.nu)),
		u"Да!" : (bot.reply_to, message, random.choice(dialogs.da)),
		u"блять" : (bot.reply_to, message, random.choice(dialogs.blyat)),
		u"Андрей" : (bot.reply_to, message, random.choice(dialogs.andrey)),
		u"хуесос" : (bot.reply_to, message, random.choice(dialogs.huesos)),
		u"водк" : (bot.reply_to, message, random.choice(dialogs.vodka)),
		u"готов" : (bot.reply_to, message, random.choice(dialogs.gotov)),
		u"интересно" : (bot.reply_to, message, random.choice(dialogs.interesno)),
		u"хуй на" : (bot.reply_to, message, random.choice(dialogs.huyna)),
        u"маму" : (bot.reply_to, message, "ЕБАЛ")
    }

    if flood_meter.flood_rate <= constantsss.flood_limit:
        for i in commands:
            if i in message.text.lower():
                commands[i][0](commands[i][1], commands[i][2])

bot.polling(none_stop=True)
