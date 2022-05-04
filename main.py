import discord
import os

class Settings:
  Prefix = os.getenv("PREFIX")
  Token = os.getenv("TOKEN")
  Embed_color = os.getenv("COLOR")

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
       if message.author == self.user:
            return
       if message.content.startswith(Settings.Prefix + 'hello'):
            await message.channel.send('Hello World!')
         
       if message.content.startswith(Settings.Prefix + 'ping'):
         await message.channel.send('Pong!')

client = MyClient()
client.run(Settings.Token)
