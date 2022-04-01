import discord
import json
from discord.ext import commands

prefix = "!bx"

TOKEN = "Your-Bot-Token-Goes-Here"

client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name= 'BLUExVENOM on YouTube'))
    print("{0.user} is now online!".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!bx Hello'):
        await message.channel.send('Hello there!')
        
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('!bx Bye'):
        await message.channel.send('BYE') 

client.run(TOKEN)


