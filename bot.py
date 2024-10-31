import discord
import asyncio
import os
from config import *
from discord.ext import commands

# Intents
intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents, help_command=None)

# Cogs
async def load_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try:
                await bot.load_extension(f'cogs.{filename[:-3]}')
                print(f"Loaded cog: {filename}")
            except Exception as e:
                print(f"Failed to load cog {filename}: {e}")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    await load_cogs()

@bot.command()
async def hello(ctx):
    print(f'User: {ctx.author.name} executed the Hello command.')
    await ctx.send('Hello!')

async def main():
    await load_cogs()
    await bot.start(TOKEN)

# Run the bot
asyncio.run(main())