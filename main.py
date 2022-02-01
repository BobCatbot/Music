import discord, os, json, asyncio
from discord.ext import commands
from modules import bot as b

client = commands.Bot(command_prefix="-", case_insensitive=True)
client.remove_command("help")

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord')


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")
        print(f"./cogs/{filename} has loaded")


client.loop.create_task(b.chpr(client))
client.run("Token")