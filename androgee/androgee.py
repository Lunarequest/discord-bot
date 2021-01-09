import os
import random
import logging
import discord
from discord.ext import commands


logging.basicConfig(level=logging.WARNING)
bot = commands.Bot(command_prefix=os.environ["DISCORD_PREFIX"])
mod_role_id = os.environ["mod_role_id"]
mod_role_name = os.environ["mod_role_name"]
mod_deined_message = "you are not a moderator"


@bot.event
async def on_ready():
    print(f"We is logged in as {bot.user}")


@bot.command(name="spray", aliases=["spritzered"])
async def spray(ctx, member: discord.Member = None):
    image = get_image(ctx)
    if member == None:
        await ctx.send(file=image)
    else:
        message = f"{member.mention} was sprirzered by {ctx.message.author.mention}"
        await ctx.send(message, file=image)


@bot.command(name="bonk")
async def spray(ctx, member: discord.Member = None):
    image = get_image(ctx)
    if member == None:
        await ctx.send(file=image)
    else:
        message = f"{member.mention} was bonked by {ctx.message.author.mention}"
        await ctx.send(message, file=image)


@bot.command(name="kick")
@commands.has_any_role(mod_role_id, mod_role_name)
async def kick(ctx, member: discord.Member, *, reason=None):
    try:
        await member.kick(reason=reason)
    except commands.MissingRole:
        await ctx.send(mod_deined_message)


@bot.command(name="ban")
@commands.has_any_role(mod_role_id, mod_role_name)
async def ban(ctx, member: discord.Member, *, reason=None):
    try:
        await member.ban(reason=reason)
    except commands.MissingRole:
        await ctx.send(mod_deined_message)


@bot.command(name="unban")
async def unban(ctx, *, member):
    if mod_role_id in [y.id for y in ctx.author.roles]:
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")
        for ban_entery in banned_users:
            user = ban_entery.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unbans(user)
                await ctx.send(f"unbanned {user.name}#{user.discriminator}")
    else:
        await ctx.send("you are not a moderator")


@bot.command(name="purge", aliases=["clear"])
async def purge(ctx, ammount=5):
    ammount = ammount + 1
    if mod_role_id in [y.id for y in ctx.author.roles]:
        await ctx.channel.purge(limit=ammount)


@bot.command(name="source", aliases=["sauce"])
async def source(ctx):
    message = f"{ctx.author.mention} the source is at https://github.com/advaithm/discord-bot/tree/nekos-bot"
    await ctx.send(message)


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
