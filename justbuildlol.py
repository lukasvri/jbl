import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'du er deilig')
    print('Sent message to ' + member.name)
@client.event
async def on_ready():
    await client.change_presence(game=Game(name='Beste bot i verden laga av JBL Blinks aka lukas'))
    print('Ready') 


@client.event
async def on_message(message):
    if message.content == '!fortnite':
        await client.send_message(message.channel,'fortnite is a fucking game')
    if message.content == '!eskil3':
        em = discord.Embed(description='her er eskil sundli')
        em.set_image(url='https://cdn.discordapp.com/attachments/496772516476616705/537711539218808843/AIbEiAIAAAAhCLTfmIS-q7HGEhDKka2ltNytsVgYw4WkpPf-0KOgATABjzr-488uwJxCIkfUOq5RAXagrpA.png')
        await client.send_message(message.channel, embed=em)
    if ('hoe') in message.content:
       await client.delete_message(message)
    if message.content.startswith('!dick'):
        randomlist = ["8==============D you got a big dick","8=D you got a very small dick","8=========================================================================================================================================================================================D OMG",]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('!hei bot'):
        await client.send_message(message.channel,'what do you want blitch? <@%s>'  %(message.author.id))
    if message.content == '!info':
        await client.send_message(message.channel,'JBL Blinks lagde og koda denna boten vist du lurer')
    if message.content == '!lukas':
        em = discord.Embed(description='her er lukas vestre')
        em.set_image(url='https://cdn.discordapp.com/attachments/496772516476616705/537716207542075414/37672567_432895720544356_7874540263375372288_n.png')
        await client.send_message(message.channel, embed=em)
    if message.content == '!haha,,':
        em = discord.Embed(description='her er knut-erik søvik')
        em.set_image(url='https://cdn.discordapp.com/attachments/537696375236984832/537721068278775809/48370442_10156637586231955_7382938998164946944_n.png')
        await client.send_message(message.channel, embed=em)
    if message.content == '!off':
        await client.send_message(client.get_channel('538002484342292498'), 'Bot going offline')
    if message.content == '!on':
        await client.send_message(client.get_channel('538002484342292498'), 'Bot going online')       
    if message.content.startswith('!eskil2'):
        randomlist = ["https://cdn.discordapp.com/attachments/538002484342292498/541001991862747137/MicrosoftTeams-image.png","https://cdn.discordapp.com/attachments/405815733583609876/537998093061455876/WIN_20190124_15_11_06_Pro.jpg","https://cdn.discordapp.com/attachments/496772516476616705/537711539218808843/AIbEiAIAAAAhCLTfmIS-q7HGEhDKka2ltNytsVgYw4WkpPf-0KOgATABjzr-488uwJxCIkfUOq5RAXagrpA.png",]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content == '!eskil':
        em = discord.Embed(description='her er eskil sundli')
        em.set_image(url="https://cdn.discordapp.com/attachments/538002484342292498/541001991862747137/MicrosoftTeams-image.png""https://cdn.discordapp.com/attachments/405815733583609876/537998093061455876/WIN_20190124_15_11_06_Pro.jpg""https://cdn.discordapp.com/attachments/496772516476616705/537711539218808843/AIbEiAIAAAAhCLTfmIS-q7HGEhDKka2ltNytsVgYw4WkpPf-0KOgATABjzr-488uwJxCIkfUOq5RAXagrpA.png")
    if message.content.startswith('!spill'):
        randomlist = ["jc3","roe","ow","fortnite","fivem","gta5","subnautica","cs-go","minecraft"]
        await client.send_message(message.channel,(random.choice(randomlist)))
client.run('NTM3NDEyMzEwMzQwMjA2NjAz.Dyk8dg.egVSRHJEjClJZhhjh9LUliBLhGw')
