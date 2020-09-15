import random
from discord.ext import commands

class Command(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Roll
    @commands.command()
    async def roll(self, ctx, number: int, sides: int):
        dice = [
            str(random.choice(range(1, sides + 1)))
            for _ in range(number)
        ]
        await ctx.send(' - '.join(dice))

def setup(bot):
    bot.add_cog(Command(bot))