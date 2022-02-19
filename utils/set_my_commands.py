from loader import bot
from telebot.types import Message, BotCommand

def set_my_commands():
    bot.set_my_commands([
        BotCommand('start', 'Botni qayta ishga tushurish'),
        BotCommand('help', 'Yordam bering'),
        ])