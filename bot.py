from loader import bot 
import utils
import handlers

def on_startup():
    utils.notify_admins("Bot ishga tushurildi")
    utils.set_my_commands()
    bot.infinity_polling(skip_pending=True)

on_startup()