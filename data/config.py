"""
.env fayli ichida saqlangan malumotlarni olib kelishi uchun
"""

from environs import Env

env = Env()
env.read_env()

TOKEN = env.str("TOKEN")
ADMINS = env.list("ADMINS")
ip = env.str("ip")