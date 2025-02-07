import config


import discord
from discord import app_commands
from discord.ext import commands
import random
import os
import asyncio
from datetime import datetime, timedelta

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

class MyClient(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

client = MyClient()

@client.event
async def on_ready():
    print("The bot is now ready")
    print("-----------------------------------")


@client.tree.command(name="hello", description="Greeting")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("Hello!")

@client.tree.command(name="myriceiscold", description="Well too fucking bad")
async def rice(interaction: discord.Interaction):
    await interaction.response.send_message("Well, eat faster dumbass")


client.run(config.api_key)
