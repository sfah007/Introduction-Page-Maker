#!/usr/bin/env python
# -*- coding: utf-8 -*-
import contextlib

import telebot,requests
from telebot import types

token = ' #enter your bot token here! '
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    first = message.chat.first_name

    bot.send_photo(message.chat.id, 'https://t.me/mbttt/7' ,caption=f'Hi {first}, Send your data like same as the photo!..\n\n|name|discription|instagram|.......')


@bot.message_handler(func=lambda m: True)
def Get(message):
    try:
        msg = message.text

        data = str(msg).split('|')

        name = data[1]
        discription = data[2]
        instagram = data[3]
        snapchat = data[4]
        telegram = data[5]
        twitter = data[6]
        locashion = data[7]

        bot.send_message(message.chat.id, text="Alright. I am making your website please wait")

        url = f'https://apis.red/api/make-page/?name={name}&discription={discription}&instagram={instagram}&snapchat={snapchat}&telegram={telegram}&twitter={twitter}&locashion={locashion}'
        req = requests.get(url).json()
        your_page = req['url']

        bot.send_message(message.chat.id, text=f"*Your Page Url*: {your_page}", parse_mode="markdown",disable_web_page_preview=True)
    except:
        bot.send_message(message.chat.id, text=f"sorry! you leave something empty!\nplease do /start again and make sure you fill all requires")

bot.polling(True)