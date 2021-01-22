import discord
import os
from dotenv import load_dotenv

load_dotenv()

# Get the discordpy API token
token_file = open("token.txt", "r")
tokens = token_file.readlines()
DISCORD_TOKEN = tokens[0].rstrip()

# The actual bot
bot = discord.Client()

# Detect when bot is online
@bot.event
async def on_ready():
	guild_count = 0
	for guild in bot.guilds:
		guild_count += 1
	print("The bot is in " + str(guild_count) + " guilds.")

# Read through the messages and interact with specified tests
@bot.event
async def on_message(message):
    txt = message.content.lower()
    if "fact" in txt:
        await message.channel.send("The largest salad ever made was 44,312 lb 14 oz!!")
    elif "salad bot is live" in txt:
        await message.channel.send("Hello :supreme_F:lems. Ready for some salad @everyone?!?!?!")
    elif "what a great bot" in txt:
        await message.channel.send('I know, right? <@802097431705026602> 😊🥗')
    if "salad" in txt:
        await message.add_reaction('🥗')
    # ❤😊😘🌹✔👀🎉🥑🥒🥕🍅🍴🦐🥬🥦

# Start the bot
bot.run(DISCORD_TOKEN)
