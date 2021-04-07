from discord.ext import commands
import discord
import json

with open("src/data.json","r") as JsonFile:
    data = json.load(JsonFile)

@commands.command(name="rules")
async def rules(ctx,*args):
    pass

@commands.command(name='rule')
async def rule(ctx,*args):
    array = ctx.message.content.split()
    try:
        index = int(array[1])
    except:
        if len(array) == 1:
            error_message = f"Error. Invalid argument for `<index>` parameter.\nNo argument given for `$rule`."
        else:
            error_message = f"Error. Invalid argument for `<index>` parameter.\nFailed to convert '`{ctx.message.content.split()[1]}`' to int."
        error_embed = discord.Embed(title=":x: Naw.",description=error_message,color=0xff0000)
        error_embed.add_field(name="Correct Usage:-", value="```$rule <index>```", inline=False)
        await ctx.send(embed=error_embed)
        return
    
    if index > len(data["rules"]):
        error_message = f"Error. Invalid argument for `<index>` parameter.\nIndex Out of Range."
        error_embed = discord.Embed(title=":x: Nope.",description=error_message,color=0xff0000)
        error_embed.add_field(name="Correct Usage:-", value="```$rule <index>```", inline=False)
        await ctx.send(embed=error_embed)
        return
    rule_embed = discord.Embed(title="Rules.",description=data["rules"][index-1],color=0x00cc00)
    rule_embed.set_footer(text=ctx.guild.name)
    await ctx.send(embed=rule_embed)

def setup(bot):
    bot.add_command(rule)
    bot.add_command(rules)