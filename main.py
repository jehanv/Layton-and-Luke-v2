#!/usr/local/bin/python3.10

import naff
from naff import Client, Intents, Activity, ActivityType
import logging

intents = Intents.ALL


bot = Client(default_prefix='!', sync_interactions=True, intents=intents, fetch_members=True, activity=Activity.create(name="over Laytonvivor", type=ActivityType.WATCHING))
TOKEN = "ODA1MjU1NzMyNjI2NDU2NTg2.Gt7YT3.WdHmvrRNDbnttVYD47jLt52CfKc5aKEZSTqtj0"

bot.load_extension("guild_logging")
bot.load_extension("radio")

bot.start(TOKEN)