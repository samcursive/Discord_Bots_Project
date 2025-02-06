import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from discord import Interaction

# Load the contents of dot env
load_dotenv()

intents = discord.Intents.default       #permission sets to dicord. 
intents.message_content = True          #messsage contents (read, write messages) stuff is true. 
TOKEN = os.getenv("discord_token")

