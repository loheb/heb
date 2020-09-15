import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

class Command(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Kick
    @commands.command()
    @has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'Kicked {member.mention}')


def setup(bot):
    bot.add_cog(Command(bot))