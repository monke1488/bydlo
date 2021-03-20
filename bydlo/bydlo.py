import discord
import json
import requests
import random
from discord.ext import commands
from discord import FFmpegPCMAudio
import asyncio

# suka_json="""
# {
# "response":{
#  "count": 53245
#  }
# }
#  """






# data = json.loads(suka_json)


# with open('suka.json', 'w+') as file:
#         json.dump(data,file)


bot = commands.Bot(command_prefix='>')

@bot.event
async def on_ready():
    print('асалям')



@bot.command(pass_context=True)
async def hohol(ctx):
    if ctx.author.id == 695330777545834647:
            await ctx.channel.send('соси')
    elif (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('hohol.mp3')
        player = voice.play(source)
        player.start()
        while not player.is_done():
                await asyncio.sleep(10)
        player.stop()
        await voice.disconnect()
    else:
        await ctx.send('в голосовой зайди ебло)')

@bot.command(name='monke')
async def randimg(ctx):
    if ctx.author.id == 695330777545834647:
            await ctx.channel.send('соси')
    else:
        images = ['6quii5Zg_400x400.jpg','M-YnMbnh_400x400.jpg', 'aMLNBRcbuSo.jpg']
        random_image = random.choice(images)
        await ctx.send(file=discord.File(random_image))


@bot.command()
async def fox(ctx):
    if ctx.author.id == 695330777545834647:
            await ctx.channel.send('соси')
    else:
        response = requests.get('https://some-random-api.ml/img/fox')
        json_data = json.loads(response.text) 

        embed = discord.Embed(color = 0xff9900, title = 'Random Fox') 
        embed.set_image(url = json_data['link']) 
        await ctx.send(embed = embed) 


@bot.command()
async def dog(ctx):
    if ctx.author.id == 695330777545834647:
            await ctx.channel.send('соси')
    else:
        response = requests.get('https://some-random-api.ml/img/dog') 
        json_data = json.loads(response.text) 

        embed = discord.Embed(color = 0xff9900, title = 'Random dog') 
        embed.set_image(url = json_data['link']) 
        await ctx.send(embed = embed)


@bot.command()
async def саша(ctx):
    if ctx.author.id == 695330777545834647:
            await ctx.channel.send('соси')
    else:
        await ctx.send('лапочка)')


@bot.command()
async def казл(ctx):
    if ctx.author.id == 695330777545834647:
            await ctx.channel.send('соси')
    else:
        await ctx.send('лох')


@bot.command()
async def сифон(ctx):
    if ctx.author.id == 695330777545834647:
            await ctx.channel.send('соси')
    else:
        await ctx.send('сифонит ежи')


bot.run('ODEzNzU3MTAzNzc1OTQwNjM4.YDT8XA.h251eBG6rA8xJUZNeQDMovFig4Q')
