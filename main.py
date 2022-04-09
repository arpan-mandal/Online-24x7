import discord
import os
import keep_alive
from discord.ext import commands

client = commands.Bot(command_prefix='lmao, change nothing here!', self_bot=True, help_command=None)

async def on_ready():
  await client.change_presence(status=discord.Status.online, activity=discord.Game("I am going to give you up"))

keep_alive.keep_alive()
client.run(os.getenv("TOKEN"), bot=False)
