import os
from discord.ext import commands
from discord.ext.commands import has_permissions

bot = commands.Bot(command_prefix='!', case_insensitive=True)

@bot.command()
@has_permissions(administrator=True)
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.send ('Command has been loaded.')

@bot.command()
@has_permissions(administrator=True)
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send('Command has been unloaded.')

for filename in os.listdir(path='./code/cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
               
bot.run(os.enivorn[TOKEN])  
