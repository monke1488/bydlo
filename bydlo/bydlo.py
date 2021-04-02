import discord
import requests
import random
from discord.ext import commands
from discord import FFmpegPCMAudio
import asyncio
import json
import datetime
from encoderrr import Message, MyEncoder

images = ['6quii5Zg_400x400.jpg','M-YnMbnh_400x400.jpg', 'aMLNBRcbuSo.jpg']

id_deb = [695330777545834647, 630864081468915741, 523383507888898050, 632572681757392896]

data = {"харча": []}

bot = commands.Bot(command_prefix='>')


@bot.event
async def on_message(message):
    split_message = message.content.split()
    if len(split_message) == 0:
        return None
    msg = Message(message.author, message.content)
    data["харча"].append(msg)
    await bot.process_commands(message)



@bot.event
async def on_disconnect():
    time = datetime.datetime.now()
    print('bydlo disconnect at {}'.format(time))
    with open('musor.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, cls=MyEncoder, indent=4, ensure_ascii=False)


@bot.command(name='абоба')

@commands.is_owner()
async def bot_shutdown(ctx):
    await ctx.bot.logout()


@bot.event
async def on_ready():
    print('асалям')



@bot.command(pass_context=True)
async def hohol(ctx):
    if ctx.author.id in id_deb:
            await ctx.channel.send('соси')
    elif (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('hohol.mp3')
        player = voice.play(source)
        player.start()
        while not player.is_done():
                await asyncio.sleep(1)
        player.stop()
        await voice.disconnect()
    else:
        await ctx.send('в голосовой зайди ебло)')


@bot.command(name='monke')
async def randimg(ctx):
    if ctx.author.id in id_deb:
            await ctx.channel.send('соси')
    else:
        random_image = random.choice(images)
        await ctx.send(file=discord.File(random_image))


@bot.command()
async def fox(ctx):
    if ctx.author.id in id_deb:
            await ctx.channel.send('соси')
    else:
        response = requests.get('https://some-random-api.ml/img/fox')
        json_data = json.loads(response.text) 

        embed = discord.Embed(color = 0xff9900, title = 'Random Fox') 
        embed.set_image(url = json_data['link']) 
        await ctx.send(embed = embed) 


@bot.command()
async def dog(ctx):
    if ctx.author.id in id_deb:
            await ctx.channel.send('соси')
    else:
        response = requests.get('https://some-random-api.ml/img/dog') 
        json_data = json.loads(response.text) 

        embed = discord.Embed(color = 0xff9900, title = 'Random dog') 
        embed.set_image(url = json_data['link']) 
        await ctx.send(embed = embed)


@bot.command()
async def саша(ctx):
    if ctx.author.id in id_deb:
            await ctx.channel.send('соси')
    else:
        await ctx.send('лапочка)')


@bot.command()
async def казл(ctx):
    if ctx.author.id in id_deb:
            await ctx.channel.send('соси')
    else:
        await ctx.send('лох')


@bot.command()
async def сифон(ctx):
    if ctx.author.id in id_deb:
            await ctx.channel.send('соси')
    else:
        await ctx.send('сифонит ежи')


bot.run('ODEzNzU3MTAzNzc1OTQwNjM4.YDT8XA.rejjhQ-e4kUAviT4CJyeAVrbil4')
