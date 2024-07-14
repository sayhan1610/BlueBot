import discord
import random
import asyncio
from discord.ext import commands, tasks
from itertools import cycle

token = "token here"

bot = commands.Bot(command_prefix="b.", intents=discord.Intents.all())
status = cycle([
    discord.Activity(type=discord.ActivityType.watching, name="the ocean"),
    discord.Activity(type=discord.ActivityType.watching, name="out for /help"),
    discord.Activity(type=discord.ActivityType.listening, name="the ocean's whispers")
])

@bot.event
async def on_ready():
    change_status.start()
    print("Bot is up & ready!")
    try:
        synced = await bot.sync_commands()
        if synced is not None:
            print(f"Synced {len(synced)} command(s)")
        else:
            print("Failed to sync commands. No commands synced.")
    except discord.errors.HTTPException as e:
        print(f"HTTP error while syncing commands: {e}")
    except discord.errors.Forbidden as e:
        print(f"Missing permissions to sync commands: {e}")
    except Exception as e:
        print(f"Error syncing commands: {e}")

@tasks.loop(seconds=15)
async def change_status():
    activity = next(status)
    await bot.change_presence(status=discord.Status.idle, activity=activity)

@bot.slash_command(name="ping", description="Test the bot ping")
async def ping(ctx):
    latency = bot.latency * 1000  # in milliseconds
    await ctx.respond(f"The current ping is **{latency:.2f}** ms! <:jojos_tom:1071123688201662535>", ephemeral=True)

bot.run(token)
