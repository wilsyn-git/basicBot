#!/usr/bin/env python3
import os
import discord
import random
import math

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print("Bot is Ready!")

@bot.event
async def on_message(msg):
    if msg.author == bot.user:
        return
    
    if msg.content == 'tell me a dad joke':
    dad_jokes = [
        "How do you get a squirrel to like you? Act like a nut.",
        "Why don't eggs tell jokes? They'd crack each other up.",
        "I don't trust stairs. They're always up to something.",
    ]
    response = random.choice(dad_jokes)
    await msg.channel.send(response)


    if msg.content == 'blah':
        response = "don\'t be sad"
        await msg.channel.send(response)

    if msg.content == 'why am i?':
        response = f'You exist to communicate with a bot'
        await msg.channel.send(response)

    if msg.content == 'who am i?':
        response = f'You are {msg.author.name}'
        await msg.channel.send(response)
    await bot.process_commands(msg)

@bot.command(name='repeat', help='repeats what you typed')
async def repeat(ctx, *args):
    await ctx.send('{}'.format(' '.join(args)))

@bot.command(name='bot', help='this does very little')
async def isbot(ctx):
    pile_of_stuff = [
        'i am not a bot',
        'ok, maybe i\'m a bot',
        'definitely a bot',
    ]

    response = random.choice(pile_of_stuff)
    await ctx.send(response)

@bot.command(name='roll', help='Usage: roll <numDice> <numSides>')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    sum = 0
    mult = 1
    if (number_of_dice <= 0 or number_of_sides == 0):
        dice = ["no"]
        await ctx.send(', '.join(dice))
    else:
        if (-1 * number_of_sides > 0):
            mult = -1
        number_of_sides = abs(number_of_sides)
        dice = [
            str(mult * random.choice(range(1,number_of_sides+1)))
            for _ in range(number_of_dice)
        ]
        for die in dice:
            sum = sum + int(die)
        await ctx.send(', '.join(dice) + " and the sum is: " + str(sum))


@bot.command(name='crunchyroll', help='sure why not')
async def crunchy(ctx):
    response = "This is not a command"
    await ctx.send(response)

bot.run(TOKEN)
