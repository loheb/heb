import discord
from discord.ext import commands

class Command(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Say
    @commands.command()
    async def say(self, ctx, arg: commands.clean_content):
        await ctx.send(arg)


def setup(bot):
    bot.add_cog(Command(bot))