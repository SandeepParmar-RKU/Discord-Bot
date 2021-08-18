import discord
import random
import os
from discord.ext import commands,tasks
from itertools import cycle
intents=intents=discord.Intents.all()

client = commands.Bot(command_prefix='.',intents=intents)
#Status = cycle (['s'],[''])

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle,activity=discord.Game('Always Pleasure!'))
    print('ready')


@client.event
async def on_member_join(member):
    await member.send(f'Welcome! {member.name} now pull yourself together you look like homeless magician!')
    print('new joined',member.name)


@client.event
async def on_member_remove(ctx,member):
    await ctx.send(f'Goodbye {member}')

@client.command()
async def ping(ctx):
    await ctx.send(f'{round(client.latency*1000)}ms Well very bad for heaven P.S. it does not mean anything')

@client.command(aliases=['8ball','test'])
async def _8ball(ctx,*,question):
    responses = ['● It is certain.',
                 '● It is decidedly so.',
                 '● Without a doubt.',
                 '● Yes – definitely.',
                 '● You may rely on it.',
                 '● As I see it, yes.',
                 '● Most likely.',
                 '● Outlook good.',
                 '● Yes.',
                 '● Signs point to yes.',
                 '● Reply hazy, try again.',
                 '● Ask again later.',
                 '● Better not tell you now.',
                 '● Cannot predict now.',
                 '● Concentrate and ask again.',
                 '● Do not count on it.',
                 '● My reply is no.',
                 '● My sources say no.',
                 '● Outlook not so good.',
                 '● Very doubtful.',
                ]
    await ctx.send(f'{random.choice(responses)}')

@client.command()
async def clear(ctx,amount=10):
    await ctx.channel.purge(limit=amount)

@client.command()
async def kick(ctx,member:discord.Member,*,reason=None,):
    await member.kick(reason=reason)


@client.command()
async def ban(ctx,member:discord.Member,*,reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Punished {member.mention}')

@client.command()
async def unban(ctx,*,member):
    banned = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned:
        user = ban_entry.user

        if(user.name,user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Pull yourself together. You look like a homeless magician! {user.mention}')
            return

@client.command()
async def load(ctx,extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx,extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
async def reaload(ctx,extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
            
client.run('NzI0ODcwODMxNDY0OTA2ODc0.XvGekQ.IKHSZYpsKsgpw0JnBDCQAQKBq_Q')