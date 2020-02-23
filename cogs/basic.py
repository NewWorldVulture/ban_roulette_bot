import discord
from discord.ext import commands
from datetime import datetime as d

# New - The Cog class must extend the commands.Cog class
class Basic(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='about',
        description='The about command'
    )
    async def about_command(self, message):
        # About command that spews useful information about the bot.

        help_embed = discord.Embed(
            title="Ban Roulette Discord Bot",
            description="The Ban Roulette Discord Bot is a bot that bans you upon request.",
            colour=discord.Colour.blue()
            )  # Embed that's sent back to the user.

        # I'm cheating here a bit cause I couldn't figure out how to call for PREFIX directly.
        commands_list = """**Current Prefix:** `~`
        `about` - Shows this message
        `ban roulette <chambers>` - Has a 1/chambers chance of banning you! fun!
        `ban me` - The nuclear option. Immediately bans you upon request"""

        help_embed.add_field(name="Commands", value=commands_list)  # Add a field of available commands for the bot.

        await message.channel.send(embed=help_embed)  # Sends the help_embed to the channel the command was called.


def setup(bot):
    bot.add_cog(Basic(bot))
    # Adds the Basic commands to the bot
    # Note: The "setup" function has to be there in every cog file
