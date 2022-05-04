import discord
import os
import requests


client = discord.Client()



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

    await client.change_presence(activity=discord.Game('Boolean'))

prefix = os.getenv("PREFIX")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(prefix + 'hello'):
        await message.channel.send('Hello!')

client.run(os.getenv("TOKEN"))
