#!/usr/local/bin/python3.10

import naff
from naff import Client, Intents, Activity, ActivityType
import logging

intents = Intents.ALL


bot = Client(default_prefix='!', sync_interactions=True, intents=intents, fetch_members=True, activity=Activity.create(name="over Laytonvivor", type=ActivityType.WATCHING))
TOKEN = ""

bot.load_extension("application")
bot.load_extension("guild_logging")
bot.load_extension("radio")
bot.load_extension("roles")

bot.start(TOKEN)
