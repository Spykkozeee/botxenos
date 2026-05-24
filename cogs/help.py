import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    async def help(self, ctx, *, categorie: str = None):
        if categorie is None:
            embed = discord.Embed(
                title="🤖 MALA Bot — Aide",
                description="Bot gaming du serveur MALA. Toutes les commandes disponibles :",
                color=0x5865F2
            )
            embed.add_field(
                name="🔫 Call of Duty",
                value="`!help cod` pour les détails\n`!cod meta` `!cod zombies` `!cod news` `!cod build`",
                inline=False
            )
            embed.add_field(
                name="⚔️ TESO",
                value="`!help teso` pour les détails\n`!teso builds` `!teso dps` `!teso heal` `!teso tank` `!teso news`",
                inline=False
            )
            embed.add_field(
                name="🌙 Elden Ring Nightreign",
                value="`!help elden` pour les détails\n`!elden builds` `!elden guide` `!elden boss` `!elden news`",
                inline=False
            )
            embed.add_field(
                name="🔪 Dead by Daylight",
                value="`!help dbd` pour les détails\n`!dbd killers` `!dbd survivors` `!dbd perks` `!dbd news`",
                inline=False
            )
            embed.add_field(
                name="🐉 Dokkan Battle",
                value="`!help dokkan` pour les détails\n`!dokkan teams` `!dokkan tips` `!dokkan news`",
                inline=False
            )
            embed.add_field(
                name="👥 LFG — Chercher des joueurs",
                value="`!help lfg` pour les détails\n`!lfg create` `!lfg list` `!lfg join` `!lfg leave`",
                inline=False
            )
            embed.set_footer(text="MALA Bot • Tape !help <catégorie> pour plus de détails")
            await ctx.send(embed=embed)

        elif categorie.lower() == "cod":
            embed = discord.Embed(title="🔫 Call of Duty — Commandes", color=0xFF6600)
            embed.add_field(name="`!cod`", value="Menu principal COD", inline=False)
            embed.add_field(name="`!cod meta`", value="Tier list armes multi (S/A/B/C)", inline=False)
            embed.add_field(name="`!cod zombies`", value="Stratégie et builds Zombies", inline=False)
            embed.add_field(name="`!cod news`", value="Dernières actualités et patches", inline=False)
            embed.add_field(name="`!cod build <arme>`", value="Build recommandé pour une arme (ex: `!cod build hrm-9`)", inline=False)
            await ctx.send(embed=embed)

        elif categorie.lower() == "teso":
            embed = discord.Embed(title="⚔️ TESO — Commandes", color=0xAA6600)
            embed.add_field(name="`!teso`", value="Menu principal TESO", inline=False)
            embed.add_field(name="`!teso builds`", value="Tous les builds méta par rôle", inline=False)
            embed.add_field(name="`!teso dps`", value="Builds DPS détaillés", inline=False)
            embed.add_field(name="`!teso heal`", value="Builds Healer détaillés", inline=False)
            embed.add_field(name="`!teso tank`", value="Builds Tank détaillés", inline=False)
            embed.add_field(name="`!teso news`", value="Dernières actualités TESO", inline=False)
            await ctx.send(embed=embed)

        elif categorie.lower() == "elden":
            embed = discord.Embed(title="🌙 Elden Ring Nightreign — Commandes", color=0xCC8800)
            embed.add_field(name="`!elden`", value="Menu principal Elden Ring", inline=False)
            embed.add_field(name="`!elden builds`", value="Builds méta complets", inline=False)
            embed.add_field(name="`!elden guide`", value="Guide Nightreign + tips essentiels", inline=False)
            embed.add_field(name="`!elden boss`", value="Nightlords et conseils pour les battre", inline=False)
            embed.add_field(name="`!elden news`", value="Dernières actus Elden Ring", inline=False)
            await ctx.send(embed=embed)

        elif categorie.lower() == "dbd":
            embed = discord.Embed(title="🔪 Dead by Daylight — Commandes", color=0xCC0000)
            embed.add_field(name="`!dbd`", value="Menu principal DBD", inline=False)
            embed.add_field(name="`!dbd killers`", value="Tier list des killers", inline=False)
            embed.add_field(name="`!dbd survivors`", value="Tier list des survivors", inline=False)
            embed.add_field(name="`!dbd perks`", value="Top perks méta killer & survivor", inline=False)
            embed.add_field(name="`!dbd killer <nom>`", value="Détails d'un killer (ex: `!dbd killer Nurse`)", inline=False)
            embed.add_field(name="`!dbd news`", value="Dernières actus DBD", inline=False)
            await ctx.send(embed=embed)

        elif categorie.lower() == "dokkan":
            embed = discord.Embed(title="🐉 Dokkan Battle — Commandes", color=0xFF6600)
            embed.add_field(name="`!dokkan`", value="Menu principal Dokkan", inline=False)
            embed.add_field(name="`!dokkan teams`", value="Tier list des meilleures équipes", inline=False)
            embed.add_field(name="`!dokkan team <nom>`", value="Détails d'une équipe (ex: `!dokkan team Fusion`)", inline=False)
            embed.add_field(name="`!dokkan tips`", value="Conseils & astuces", inline=False)
            embed.add_field(name="`!dokkan news`", value="Dernières actus et events", inline=False)
            await ctx.send(embed=embed)

        elif categorie.lower() == "lfg":
            embed = discord.Embed(title="👥 LFG — Commandes", color=0x5865F2)
            embed.add_field(name="`!lfg create <jeu> <nb> [desc]`", value="Créer un LFG (ex: `!lfg create cod 3 On cherche un 3ème !`)", inline=False)
            embed.add_field(name="`!lfg list [jeu]`", value="Voir les LFG actifs (optionnel: filtrer par jeu)", inline=False)
            embed.add_field(name="`!lfg join <id>`", value="Rejoindre un LFG existant", inline=False)
            embed.add_field(name="`!lfg leave <id>`", value="Quitter un LFG", inline=False)
            embed.add_field(name="`!lfg close <id>`", value="Fermer ton LFG (créateur uniquement)", inline=False)
            embed.add_field(name="**Jeux valides**", value="`cod` `teso` `elden` `dbd` `dokkan`", inline=False)
            await ctx.send(embed=embed)

        else:
            await ctx.send(embed=discord.Embed(
                description=f"❌ Catégorie `{categorie}` inconnue. Choix : `cod`, `teso`, `elden`, `dbd`, `dokkan`, `lfg`",
                color=0xFF4444
            ))

async def setup(bot):
    await bot.add_cog(Help(bot))
