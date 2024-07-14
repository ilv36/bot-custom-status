import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content == '.':
        await message.channel.send('Bot is now online!')
        await bot.change_presence(status=discord.Status.online, activity=None)
    elif message.content == '?':
        await message.channel.send('Bot is now idle.')
        await bot.change_presence(status=discord.Status.idle, activity=None)
    elif message.content == '!':
        await message.channel.send('Bot is now Do Not Disturb.')
        await bot.change_presence(status=discord.Status.dnd, activity=None)


bot.run("")
