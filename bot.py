import discord
from discord.ext import commands
from apod import apod
import os

client = commands.Bot(command_prefix=';')

@client.event
async def on_ready():
    print('hello world')

@client.command(aliases = ['apod'])
async def pictureOfTheDay(ctx, day: str, month: str, year: str):
    apodInfo = apod(year, month, day)
    text = apodInfo.getApod()

    #await ctx.send(text, file = discord.File('apodIMG.jpg'))
    await ctx.send(text)
    os.remove('apodIMG.jpg')
    
client.run("")
