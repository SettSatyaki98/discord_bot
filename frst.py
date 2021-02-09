# bot.py
import os

import discord
import random
from discord.ext import commands
#from dotenv import load_dotenv

#load_dotenv()
#TOKEN = os.getenv('NzM2MjQyMTE3MjgxODQxMTkz.Xxr85w.cbBGSp6duMIUKalZzTtCUefJOaI')

bot = commands.Bot(command_prefix='det ')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='face')
async def face(ctx, arg):
    await ctx.send('hi '+ arg+'!!!')
    dir = '/home/student/Pictures/dataset'
    if(os.path.isdir(dir+'/'+arg)):
        imlst = os.listdir(dir+'/'+arg)
        print('detected image list = ', imlst)
        filename = random.choice(imlst)
        print('selected file = ', filename)
        await ctx.send(file=discord.File(dir+'/'+arg+'/'+filename))

bot.run("NzM2MjQyMTE3MjgxODQxMTkz.Xxr85w.cbBGSp6duMIUKalZzTtCUefJOaI")
