import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

COGS = ["cogs.cod", "cogs.teso", "cogs.elden", "cogs.dbd", "cogs.dokkan", "cogs.lfg", "cogs.help"]

@bot.event
async def on_ready():
    print(f"✅ {bot.user} est connecté et prêt !")
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.playing,
        name="!help | MALA Bot"
    ))
    try:
        synced = await bot.tree.sync()
        print(f"✅ {len(synced)} commandes slash synchronisées")
    except Exception as e:
        print(f"❌ Erreur sync slash: {e}")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(embed=discord.Embed(
            description="❌ Commande inconnue. Tape `!help` pour voir toutes les commandes.",
            color=0xFF4444
        ))
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed=discord.Embed(
            description=f"❌ Argument manquant : `{error.param.name}`",
            color=0xFF4444
        ))
    else:
        await ctx.send(embed=discord.Embed(
            description=f"❌ Erreur : {str(error)}",
            color=0xFF4444
        ))

async def main():
    async with bot:
        for cog in COGS:
            try:
                await bot.load_extension(cog)
                print(f"✅ Cog chargé : {cog}")
            except Exception as e:
                print(f"❌ Erreur chargement {cog}: {e}")
        await bot.start(os.getenv("DISCORD_TOKEN"))

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
