import discord
from discord.ext import commands
from saucenao_api import SauceNao

class Command(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Source
    @commands.command()
    async def source(self, ctx, arg):

        sauce = SauceNao()
        results = sauce.from_url(arg)
        best = results[0]

        embed = discord.Embed(
            color=discord.Color.dark_teal()
        )

        embed.set_author(name=ctx.message.author, icon_url='{}'.format(ctx.message.author.avatar_url))
        embed.set_thumbnail(url=arg)
        embed.add_field(name='Title: {}'.format(best.title), value=best.urls, inline=False)
        embed.add_field(name='Confidence', value='Matched with a {} similarity.'.format(best.similarity), inline=False)
        embed.set_footer(text="Powered by SauceNAO")

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Command(bot))

