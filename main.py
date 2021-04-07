import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import json

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

with open("src/data.json","r") as JsonFile:
    data = json.load(JsonFile)

bot = commands.Bot(command_prefix='$')
bot.remove_command('help')

@bot.command(name='rule')
async def rule(ctx,*args):
    index = int(ctx.message.content.split()[1])
    rule_embed = discord.Embed(title="Rules.",description=data["rules"][index-1],color=0x00cc00)
    rule_embed.set_footer(text=ctx.guild.name)
    await ctx.send(embed=rule_embed)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

bot.run(TOKEN)