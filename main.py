import os
import random
from dotenv import load_dotenv
import discord
from discord.ext import commands
from discord import Interaction

# Load the contents of dot env
load_dotenv()

intents = discord.Intents.default()       #permission sets to dicord. 
intents.message_content = True          #messsage contents (read, write messages) stuff is true. 
TOKEN = os.getenv("DISCORD_TOKEN")


# Assign a function when certain commands happen
client = commands.Bot(command_prefix="?", intents=intents)


@client.event
async def on_ready():
    print(f"{client.user.name} is ready!")

client.run(token=TOKEN)


