import discord
from discord.ext import commands

class Test(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('ready test')

    @commands.command()
    async def demo(self,ctx):
        await ctx.send(f'test')

def setup(client):
    client.add_cog(Test(client))