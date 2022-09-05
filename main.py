#!/usr/local/bin/python3.10

import naff
from naff import Client, Intents
import logging

logging.basicConfig()
cls_log = logging.getLogger(naff.const.logger_name)
cls_log.setLevel(logging.DEBUG)

intents = Intents.ALL


bot = Client(default_prefix='!', sync_interactions=True, intents=intents, fetch_members=True)
TOKEN = "ODA1MjU1NzMyNjI2NDU2NTg2.Gt7YT3.WdHmvrRNDbnttVYD47jLt52CfKc5aKEZSTqtj0"

bot.load_extension("guild_logging")
bot.load_extension("radio")

bot.start(TOKEN)