import discord
from discord.ext import commands
from __main__ import bot


class Event(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Ready and Bot Status
    @commands.Cog.listener()
    async def on_ready(self):
        await bot.change_presence(status=discord.Status.online, activity=discord.Game('Use +help'))
        print('Bot is ready.')


def setup(bot):
    bot.add_cog(Event(bot))