import discord
from discord import *
from discord.ext import commands
import requests

bot = commands.Bot(command_prefix="BOT_PREFIX", intents = discord.Intents.all()) # <-----

@bot.event
async def on_ready():
    await bot.change_presence( status = discord.Status.idle, activity = discord.Game('ab/'))
    print(f'Bot: {bot.user.name} started!')

@bot.event
async def on_command_error(ctx, error):
    embederror = discord.Embed(
        title = f'Error',
        description = f'An error occurred while executing the code. Error Information: { error }. The bug has already been submitted and will be resolved soon...',
        colour = discord.Colour.from_rgb(255, 0, 0)
    )
    await ctx.send(embed=embederror)

    report_errror_channel = bot.get_channel(CHANNEL_ID) # <-----
    await report_errror_channel.send(error)

@bot.command()
async def say(ctx, *, msg):
    await ctx.send(msg)

@bot.command()
async def send_question(ctx, *, question):
    question_channel = bot.get_channel(CHANNEL_ID) # <-----

    embedquestion = discord.Embed(
        title = f'Question from {ctx.author.name}#{ctx.author.discriminator}',
        description = f' {question}',
        colour = discord.Colour.from_rgb(255, 0, 0)
    )
    await question_channel.send(embed=embedquestion)

    embedquestionsucess = discord.Embed(
        title = f'Successfully!',
        description = f'Your question has been sent',
        colour = discord.Colour.from_rgb(255, 0, 0)
    )
    await ctx.send(embed=embedquestionsucess)

# idea command
@bot.command()
async def send_idea(ctx, *, question):
    question_channel = bot.get_channel(CHANNEL_ID) # <-----

    embedquestion = discord.Embed(
        title = f'Idea from {ctx.author.name}#{ctx.author.discriminator}',
        description = f'{question}',
        colour = discord.Colour.from_rgb(255, 0, 0)
    )
    await question_channel.send(embed=embedquestion)

    embedquestionsucess = discord.Embed(
        title = f'Successfully!',
        description = f'Your idea has been submitted',
        colour = discord.Colour.from_rgb(255, 0, 0)
    )
    await ctx.send(embed=embedquestionsucess)

#  bot ping
@bot.command()
async def ping(ctx):
    await ctx.send('Pong! {0}ms'.format(round(bot.latency, 1)))

# run bot
bot.run("BOT_TOKEN")  # <-----
