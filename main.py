import discord
import os  
import random
import requests
from ai import identify
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix= '!', intents=intents)

@bot.command()
async def aicheck(ctx,file:discord.Attachment):
        await file.save(f"C:/Users/aryab/Documents/Kodland/Ai_discord_Bot/Images/{file.filename}")
        await ctx.send("Processing...")
        if file.filename.split(".")[1] == "png":
                classname, confidence_sc = identify(f"./Images/{file.filename}")
                await ctx.send(f"{classname}: {confidence_sc}")
        else:
                await ctx.send("I can't handle anything other than a png file")

        

bot.run('Insert_bot_token')
