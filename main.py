import discord
import random
import asyncio
from discord.ext import commands, tasks
from itertools import cycle
from discord.utils import format_dt
from datetime import datetime

token = "token_here" # Token for your discord bot from https://discord.com/developers/applications/
log_channel_id = 1082220200440627211  # Universal log channel for Bot. Replace with your log channel ID

# Restricted words the bot will erase
inappropriate_words = {
    "fuck", "nigga", "bitch", "asshole", "cunt", "dick", "bastard", 
    "cock", "pussy", "whore", "slut", "fag", "retard", "shit", "crap",
    "damn", "goddamn", "motherfucker", "twat", "douchebag", "wanker",
    "arsehole", "bollocks", "bellend", "knobhead", "prick", "muff", "douche",
    "boob", "tit", "turd", "wank", "piss", "arse", "fanny", "bimbo", "bogus",
    "bullshit", "bugger", "circumcise", "clitoris", "cocksucker", "cum", "cunnilingus",
    "dildo", "ejaculate", "felching", "fingerbang", "fisting", "fornicate", "gangbang",
    "glans", "jizz", "labia", "masturbate", "molest", "nympho", "orgasm", "pedophile",
    "penetrate", "phallus", "porn", "prostitute", "pubes", "queef", "rape", "rimjob",
    "scrotum", "semen", "sex", "sexual", "sodomize", "sperm", "spunk", "testicle",
    "tits", "vagina", "virgin", "wetback", "wtf", "xxx", "zoophile", "asshat",
    "bitchass", "cumdumpster", "dickhead", "douchecanoe", "fucktard", "pissflaps",
    "shiteater", "skank", "slutbag", "thundercunt", "twatlips", "whorebag", "nutting",
    "knobend", "schlong", "fuckwit", "asswipe", "cockwomble", "cuntnugget", "shithead",
    "cockjockey", "arsebiscuit", "bastardly", "fuckery", "dickish", "twatwaffle", "arsebadger",
    "pissface", "douchewaffle", "thot", "cockgobbler", "jerkoff", "fuckknuckle", "fannybaws",
    "cumbubble", "arseclown", "cockmongler", "turdnugget", "assclown", "fucknugget", "wankstain"
}


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


# Ping command
@bot.slash_command(name="ping", description="Test the bot ping")
async def ping(ctx):
    latency = bot.latency * 1000  # in milliseconds
    await ctx.respond(f"The current ping is **{latency:.2f}** ms!", ephemeral=True)


# Automod
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return  # Ignore messages sent by the bot itself

    content = message.content.lower()
    for word in inappropriate_words:
        if word in content:
            # Delete the message containing inappropriate language
            await message.delete()

            # Send a DM warning to the user
            try:
                await message.author.send("Please refrain from using inappropriate language.")
            except discord.errors.Forbidden:
                print(f"Failed to send DM warning to {message.author}")

            # Log the usage of restricted word
            log_channel = bot.get_channel(log_channel_id)
            if log_channel:
                timestamp = format_dt(datetime.utcnow(), style="f")
                await log_channel.send(f"**[{timestamp} UTC]** - **{message.author.name}** used restricted word `{word}` in <#{message.channel.id}>")

            break  # Exit loop if any inappropriate word is found

    await bot.process_commands(message)



# Say
@bot.slash_command(
    name="say",
    description="Make the bot say something in the channel."
)
async def say(ctx, thing_to_say: str):
    # Replace "\n" with newline characters
    thing_to_say = thing_to_say.replace("\\n", "\n")
    
    await ctx.send(thing_to_say)
    await ctx.response.send_message("Sent!", ephemeral=True)
    
    log_channel = bot.get_channel(log_channel_id)
    if log_channel:
        timestamp = format_dt(datetime.now(), style="f")
        await log_channel.send(f"**[{timestamp} UTC]** - **{ctx.author.name}** used /say in <#{ctx.channel.id}>")

bot.run(token)
