import discord
from discord.ext import commands
import json

config = json.loads(open('config/set.json', 'r', encoding='utf-8').read())


class deleteemojis(commands.Cog):
    def __init__(self, client):
        self.client = client

    #Delete emojis
    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author.id == int(config["sizinid"]):
           if config["names"]["patlatmamesajı"] in message.content:
                for emoji in list(message.guild.emojis):
                    try:
                        if config["required"]["butunemojilerisil"]:
                            await emoji.delete()
                    except discord.Forbidden:                         
                        continue
                    except Exception as e:
                        #print("hata : {}".format(e))
                        continue
                    
def setup(client):
    client.add_cog(deleteemojis(client))