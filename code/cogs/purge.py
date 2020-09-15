from discord.ext.commands import has_permissions, MissingPermissions
from discord.ext import commands

class Command(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Purge
    @commands.command(pass_context=True)
    @has_permissions(administrator=True)
    async def purge(self, ctx, amount=1):
        await ctx.channel.purge(limit=amount + 2)
        await ctx.send(f'Purged {amount} amount of messages!')

    @purge.error
    async def purge_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send('{}, you do not have the permissions to do that!'.format(ctx.message.author))


def setup(bot):
    bot.add_cog(Command(bot))