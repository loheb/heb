import discord
from discord.ext import commands
from __main__ import bot

class Command(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Ping
    @commands.command()
    async def ping(self, ctx):
        embed = discord.Embed(
            color=discord.Color.dark_teal()
        )

        embed.set_author(name='Pong! \U0001F3D3')
        embed.add_field(name='Bot', value=f'{round(bot.latency * 1000)} ms', inline=False)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Command(bot))