import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

#Base de dados
lixos = {
    "lata": "Reciclável",
    "garrafa pet": "Reciclável",
    "papel": "Reciclável",
    "vidro": "Reciclável",
    "casca de banana": "Não reciclável",
    "resto de comida": "Não reciclável"
}

@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')

# Comando de teste
@bot.command()
async def hello(ctx):
    await ctx.send('Olá! Eu sou o bot {bot.user}!')

# Novo comando para verificar lixo
@bot.command()
async def lixo(ctx, *, item):
    item = item.lower()

# Verifica se o item existe no dicionário
    if item in lixos:
     # Mostra o resultado
        await ctx.send(item.capitalize()+ "->"+lixos[item])
    else:
    # Caso o item não esteja cadastrado
        await ctx.send("Ainda não tenho esse item cadastrado.")
