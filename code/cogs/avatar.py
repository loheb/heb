import discord
from discord.ext import commands

class Command(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Source
    @commands.command(aliases=['av', 'ava', 'avat', 'avata'])
    async def avatar(self, ctx, *, member: discord.Member):

        embed = discord.Embed(
            color=discord.Color.dark_blue()
        )
        embed.set_image(url='{}'.format(member.avatar_url))

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Command(bot))