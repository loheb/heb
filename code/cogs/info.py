import discord
from discord.ext import commands

class Command(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Info
    @commands.command()
    async def info(self, ctx, *, member: discord.Member):
        fmt = '```{0} joined on "{0.joined_at}" and has {1} roles.```'
        await ctx.send(fmt.format(member, len(member.roles)))

    @info.error
    async def info_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send('I could not find that member...')


def setup(bot):
    bot.add_cog(Command(bot))