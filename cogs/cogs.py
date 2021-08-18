import discord
from discord.ext import commands
import random
class Fun(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('ready cog')
    
    @commands.command()
    async def intro(self,ctx):
        await ctx.send(f'Name: Lucifer Morningstar :smiling_imp:  Godgiven i am afraid. Also, I’m like walking heroin. Very habit-forming. It never ends well. ')


def setup(client):
    client.add_cog(Fun(client))