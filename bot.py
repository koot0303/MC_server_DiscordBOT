import discord
# from discord import app_commands
import os
from dotenv import load_dotenv

intents = discord.Intents.all() # 権限
client = discord.Client(intents=intents)
# tree = app_commands.CommandTree(client)

# 起動時
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="マイクラサーバー起動中"))
    print(f'{client.user}起動')
    # await tree.sync() 

# 起動
load_dotenv()
TOKEN = os.environ.get('DISCORD_TOKEN')
client.run(TOKEN)
