import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def çöpünyatağınere(ctx):
    await ctx.send(f'nere')

@bot.command()
async def yer(ctx):
    await ctx.send(f'doğru konuş onu hemen çöpe at')

@bot.command()
async def hayır(ctx):
    await ctx.send(f'bruhhhhhhhh') 

@bot.command()
async def haha(ctx):
    await ctx.send(f'neyse bye kanki ama sen pissin') 

@bot.command()
async def hahabyesende(ctx):
    await ctx.send(f'biz kötüyüz aynen aynen') 

@bot.command()
async def aynen(ctx):
    await ctx.send(f'çok uzattık bye')    

@bot.command()
async def bye(ctx):
    await ctx.send(f':smiley:') 



bot.run("your")