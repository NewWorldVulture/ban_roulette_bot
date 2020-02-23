# Works with Python 3.6
import random
import asyncio
import discord
from discord.ext import commands  # Used to make commands

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PREFIX = "ban"  # Sets the prefix of the bot

LOOP = asyncio.get_event_loop()  # Creates an event loop (used to make tasks with asyncio)
channel_loop = {}  # Channel loop dictionary used to store tasks under their channel id.

bot = commands.Bot(command_prefix=PREFIX,
    description='A Discord bot to interface with the Project Euler website and provide a random set of problems.',
    case_insensitive=True)

cogs = ['cogs.basic']

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@bot.event
async def on_ready():  # Once the bot is ready:

    print("Logged in as {} - {} The bot is ready!".format(bot.user.name, bot.user.id))
    for cog in cogs:
        bot.load_extension(cog)
    game = discord.Game(name="for {}help".format(PREFIX), type=3)
    await bot.change_presence(activity=game)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@bot.event
async def on_message(message):
    """
    On every single message that the bot sees, this will trigger.
    First, it makes sure that bot doesn't reply to itself.
    Then, it makes sure that the user executing commands isn't in a DM.
    Finally, it processes commands
    """

    # Ensures that the bot doesn't reply to itself
    if message.author == bot.user:
        return

    elif not message.content.startswith("{}about".format(PREFIX)):  # If the message is not the standard about command:
        if isinstance(message.channel, discord.abc.PrivateChannel):  # If it is a private channel:
            # Tell them they can't:
            await message.channel.send("You are not allowed to call commands other than `{}about` in DMs.".format(PREFIX))
            return

    await bot.process_commands(message)  # Process commands after this is triggered (bot commands won't work without this)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@bot.event
async def on_command_error(message, exception):
    #print("Exception: {}\n\nMessage: {}".format(exception, message))
    embed = discord.Embed(title="Error from command", description=str(exception), colour=discord.Colour.red())
    print("Error with message from{}: {}\n{}".format(message.author.id, message, exception))
    await message.channel.send(embed=embed)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@bot.command(pass_context=True)
async def roulette(message, chambers=6):
    """
    ROLL THE DICE.
    """

    not_so_lucky = ["Not so lucky this time.",
                    "The regret's setting in.",
                    "Git banned, nerd.",
                    "BANNED!"]
    lucky_duck = ["Lucky Duck!",
                  "Misfire!",
                  "Die another day😎",
                  "DEAD. just kidding ur fine"]

    await message.channel.send(f"Roll the dice...")

    time.wait(3)
    banned_on_one = random.randint(chambers)
    time.wait

    target_user = message.author

    if banned_on_one == 1:
        await message.channel.send(random.choice(not_so_lucky))
        time.wait(3)
        message.author.kick(reason="Unlucky Duck")

        # Sends the user an invite back to the server
        message.bot.fetch_invite()
    else:
        await message.channel.send(random.choice(lucky_duck))


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@bot.command(pass_context=True)
async def me(message,):
    """
    Kicks the user off the discord. What do you want from me.
    """

    await message.channel.send("You got it.")
    time.wait(2)
    message.author.kick(reason="Asked for it")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TOKEN = ""

bot.run(TOKEN, bot=True, reconnect=True)  # Runs the bot
