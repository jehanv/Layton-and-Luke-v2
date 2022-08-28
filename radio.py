
import asyncio
from typing import Optional

from naff import Extension, GuildVoice, listen, slash_command, slash_option, OptionTypes, SlashCommandChoice
from naff.api.events import VoiceStateUpdate
from naff.api.voice.audio import AudioVolume
from naff.client.utils import find
from yt_dlp import YoutubeDL
from naff_audio import YTAudio

next_song = "intro"

class Radio(Extension):

    @listen()
    async def on_ready(self):
        return await self.start_radio(self.bot.get_channel(1011798163457327156))
    
    async def play_track(self):
        while True:
            audio = AudioVolume("tracks/"+next_song+".mp4")
            await self.bot.get_bot_voice_state(860674527833620480).play(audio)

    async def start_radio(self, channel: GuildVoice):
        await channel.connect(deafened=True)

    @slash_command(name="play")
    @slash_option(name="track", description="The track to play.", required=True, opt_type=OptionTypes.STRING, choices=[SlashCommandChoice(name="casino", value="casino"), SlashCommandChoice(name="chase", value="chase"), SlashCommandChoice(name="day", value="day"), SlashCommandChoice(name="illusion", value="illusion"), SlashCommandChoice(name="intro", value="intro"), SlashCommandChoice(name="layton", value="layton"), SlashCommandChoice(name="masked", value="masked"), SlashCommandChoice(name="night", value="night"), SlashCommandChoice(name="puzzle", value="puzzle")])
    async def play_new(self, ctx, track):
        global next_song
        next_song = track
        await self.bot.get_bot_voice_state(860674527833620480).stop()
        await ctx.send("Playing...", ephemeral=True)
        # await self.play_track(track)
        

def setup(bot):
    Radio(bot)