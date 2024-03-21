#bot 

import os 
import discord
from  dotenv import load_dotenv

DISCORD_TOKEN=""
GUILD = ""
load_dotenv();
Token = DISCORD_TOKEN
intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
        guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
        print(f"{client.user} has connected to discord")
        print(f'{guild.name}(id: {guild.id})')

@client.event
async def on_member_join(member):
        await member.create_dm()
        await member.dm_channel.send(
                f'hi welcome to the nullverse'
        )
        print("new user")

@client.event
async def on_message(message):
        if message.author == client.user:
                return
        boondocks_quotes = "a nigga moment"
        if message.content == 'hello':
            await message.channel.send("hey dirtbag")
client.run(Token)       