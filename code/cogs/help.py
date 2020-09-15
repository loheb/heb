import discord
from discord.ext import commands
from __main__ import bot

bot.remove_command('help')

class Command(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Help
    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(
            color=discord.Color.dark_teal()
        )

        embed.set_author(name='Command List')
        embed.add_field(name='\u200b', value='**COMMANDS USED FOR FUN**', inline=False)
        embed.add_field(name='8ball', value='Answers your questions.', inline=True)
        embed.add_field(name='say', value='Make the bot say something.', inline=True)
        embed.add_field(name='\u200b', value='**COMMANDS FOR PRACTICAL USE**', inline=False)
        embed.add_field(name='ping', value='Returns Pong!', inline=True)
        embed.add_field(name='info', value='Send info on user.', inline=True)
        embed.add_field(name='kick', value='Kick a user.', inline=True)
        embed.add_field(name='ban', value='Ban a user.', inline=True)
        embed.add_field(name='unban', value='Unban a user.', inline=True)
        embed.add_field(name='purge', value='Delete messages.', inline=True)

        await ctx.send(embed=embed)

def setup(bot):
        bot.add_cog(Command(bot))