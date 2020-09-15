import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

class Command(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Ban
    @commands.command()
    @has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention}')

def setup(bot):
        bot.add_cog(Command(bot))