import json
import discord
import queue
from discord.ext import commands

from sign.effects import *

from discord.commands.sign_control import SignControl
from sign.opc_control import OpcControl

with open('config.json', 'r') as f:
    config = json.load(f)

bot = discord.ext.commands.Bot(commands.when_mentioned_or(".sign "))


@bot.event
async def on_message(message):
    if message.author.bot:
        return
    await bot.process_commands(message)


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


bot.message_queue = queue.Queue()

bot.add_cog(SignControl(bot))
bot.add_cog(OpcControl(bot, config['opc_address']))

bot.run(config['token'])

