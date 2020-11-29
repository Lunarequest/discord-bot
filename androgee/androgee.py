import os
import random
import logging
import discord
from discord.ext import commands


logging.basicConfig(level=logging.WARNING)
bot = commands.Bot(command_prefix=os.environ["DISCORD_PREFIX"])


@bot.event
async def on_ready():
    print(f"We is logged in as {bot.user}")


@bot.command(name="spray")
async def spray(ctx, member: discord.Member = None):
    image = get_image(ctx)
    if member == None:
        await ctx.send(file=image)
    else:
        message = f"{member.mention} was sprayed by {ctx.message.author.mention}"
        await ctx.send(message, file=image)


@bot.command(name="bonk")
async def spray(ctx, member: discord.Member = None):
    image = get_image(ctx)
    if member == None:
        await ctx.send(file=image)
    else:
        message = f"{member.mention} was bonked by {ctx.message.author.mention}"
        await ctx.send(message, file=image)


def get_image(ctx):
    images = []
    files = os.walk(f"{os.path.dirname(__file__)}/media/{ctx.command}")
    for root, dirs, files in files:
        for name in files:
            images.append(f"{root}/{name}")
    loc = random.randint(0, len(images) - 1)
    img = discord.File(images[loc])
    return img


def start():
    bot.run(os.environ["DISCORD_TOKEN"])
