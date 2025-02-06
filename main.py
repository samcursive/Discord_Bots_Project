import os
import random
from dotenv import load_dotenv
import discord
from discord.ext import commands
from discord import Interaction

# Load the contents of dot env
load_dotenv()

intents = discord.Intents.default()       #permission sets to dicord. 
intents.message_content = True            #messsage contents (read, write messages) stuff is true. 
TOKEN = os.getenv("DISCORD_TOKEN")
c = 0


# Assign a function when certain commands happen
client = commands.Bot(command_prefix="?", intents=intents)


@client.event
async def on_ready():
    print(f"{client.user.name} is ready!")

#client.run(token=TOKEN)


#-------------------------------------------------------------------------
# ping commands

@client.command()
async def ping(ctx: commands.Context):
    await ctx.send("Pong!")




#-------------------------------------------------------------------------
# count commands


@client.command()
async def count(ctx: commands.Context):
    global c
    c += 1
    await ctx.send(f"Count is now: {c}")



#-------------------------------------------------------------------------
# rock paper and scissors emojis.

@client.command()
async def roshambo(ctx: commands.Context):
    choices = ["🪨","📜","✂️","🔫"]
    bot_choices = ["Rock", "Paper", "Scissors","Gun"]

    message = await ctx.send("Choose your move!")
    
    for emoji in choices: 
        await message.add_reaction(emoji)

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in choices
    



    # Try-catch block
    try: 
        reaction, user = await client.wait_for('reaction_add', timeout = 30.0, check=check)

        user_choice = None #NULL in C++
        
#    choices = ["🪨","📜","✂️","🔫"]
        if str(reaction.emoji) == "🪨":
            user_choice = "Rock"
        elif str(reaction.emoji) == "📜":
            user_choice = "Paper"
        elif str(reaction.emoji) == "✂️":
            user_choice = "Scissors"
        elif str(reaction.emoji) == "🔫":
            user_choice = "Gun"

        
        # bot choices can be made hard. 
        bot_choice = random.choice(bot_choices)


        #conditional stuff
        if user_choice == bot_choice:
            result = "**It's a tie!**"  #open and close a header in python
        
        elif (user_choice == "Rock" and bot_choice == "Scissors") or \
             (user_choice == "Scissors" and bot_choice == "Paper") or \
             (user_choice == "Paper" and bot_choice == "Rock"):
            result = f"**You Win! {user_choice} beats {bot_choice}**"

        else: 
            result = f"**You lose! {bot_choices} beats {user_choice}.**"


        await message.clear_reactions()

        await message.edit(content = f"{result}\nYou chose \"{user_choice}\".\n {client.user.name} chose \"{bot_choice}.\" ")

    except TimeoutError:
        await ctx.send("Hey this request timed out, you took too long to respond. Try again :D")

    
#-------------------------------------------------------------------------




#--------------------------------------------------------------------------------------------------------------------------------------------------

client.run(token=TOKEN)
