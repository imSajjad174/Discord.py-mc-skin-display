import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_option
from dotenv import load_dotenv
import os
import requests


load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
bot = commands.Bot(command_prefix='/', intents=intents)
slash = SlashCommand(bot, sync_commands=True)
@bot.event
async def on_ready():
    print(f'Bot is connected to {bot.user.name}')
    print('Bot is online!')






@slash.slash(name="skin", description="View and download a Minecraft player's skin")
async def skin(ctx: SlashContext, username: str):
    skin_url = f"https://minotar.net/armor/body/{username}/100.png"
    skin_download_url = f"https://minotar.net/download/{username}"
    
    embed = discord.Embed(title=f"{username}'s Minecraft Skin", description=f"Skin for {username}", color=discord.Color.blue())
    embed.set_image(url=skin_url)
    embed.add_field(name="Download", value=f"[Download {username}'s skin]({skin_download_url})")
    
    await ctx.send(embed=embed)
    
    
    
    
    
@bot.event
async def on_slash_command_error(ctx, ex):
    await ctx.send(str(ex))

bot.run(TOKEN)    
