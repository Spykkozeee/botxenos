import discord
from discord.ext import commands

ELDEN_BUILDS = [
    {"nom": "Berserker", "arme": "Greatsword", "stats": "STR 60 / END 40", "talent": "Endure + Lion's Claw", "note": "Tanky, excellent pour solo boss"},
    {"nom": "Spellsword", "arme": "Moonveil", "stats": "INT 60 / DEX 40", "talent": "Transient Moonlight + Carian Grandeur", "note": "DPS burst magique, fragile mais efficace"},
    {"nom": "Faith Paladin", "arme": "Sacred Relic Sword", "stats": "FAI 70 / VIG 40", "talent": "Wave of Gold (AoE dévastateur)", "note": "Parfait pour l'endgame et les groupes"},
    {"nom": "Bloodhound", "arme": "Rivers of Blood", "stats": "ARC 80 / DEX 40", "talent": "Corpse Piler", "note": "Top DPS saignement, très mobile"},
    {"nom": "Moonmage", "arme": "Lusat's Glintstone Staff", "stats": "INT 80 / MND 40", "talent": "Comet Azur + Terra Magica", "note": "Glass cannon, one-shot boss possible"},
]

ELDEN_NIGHTREIGN = {
    "description": "Elden Ring Nightreign est un spin-off coopératif 3v1 dans un monde généré aléatoirement.",
    "tips": [
        "🗺️ Explorer la map en priorité — les pouvoirs d'armes varient à chaque run.",
        "🤝 Coordonnez-vous pour les boss de nuit : un joueur tank, deux DPS.",
        "⚡ Gérez le cercle — il se resserre chaque nuit. Restez groupés !",
        "💀 La mort est permanente dans un run, jouez prudemment au début.",
        "🌙 Chaque Nightlord (boss final) a une mécanique unique — lisez les attaques.",
    ],
    "nightlords": [
        {"nom": "Gladius", "difficulte": "★★☆", "conseil": "Restez mobiles, évitez le centre"},
        {"nom": "Morn Ekzykes", "difficulte": "★★★", "conseil": "Dragon fire — roulez vers lui, pas à l'écart"},
        {"nom": "Sentient Pest", "difficulte": "★☆☆", "conseil": "Facile, gardez vos flasques"},
    ]
}

ELDEN_NEWS = [
    "🌙 **Nightreign** : Sortie officielle le 30 mai 2025, disponible sur PC/PS4/PS5/Xbox.",
    "🔥 **Méta actuel** : Rivers of Blood et Sacred Relic Sword dominent en builds.",
    "👥 **Co-op** : Le matchmaking 3 joueurs fonctionne sans avoir les mêmes DLC.",
    "🐉 **Nightlords** : 8 boss finaux confirmés, dont 2 non révélés avant release.",
]

class Elden(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def embed_base(self, title, color=0xCC8800):
        embed = discord.Embed(title=title, color=color)
        embed.set_footer(text="MALA Bot • Elden Ring Nightreign")
        return embed

    @commands.group(name="elden", invoke_without_command=True)
    async def elden(self, ctx):
        embed = self.embed_base("🌙 Elden Ring Nightreign — Menu")
        embed.description = (
            "`!elden builds` — Builds méta\n"
            "`!elden guide` — Guide Nightreign + tips\n"
            "`!elden boss` — Nightlords & conseils\n"
            "`!elden news` — Dernières actus"
        )
        await ctx.send(embed=embed)

    @elden.command(name="builds")
    async def elden_builds(self, ctx):
        embed = self.embed_base("⚔️ Elden Ring — Builds Méta", 0xFF8800)
        for b in ELDEN_BUILDS:
            embed.add_field(
                name=f"🗡️ {b['nom']} — {b['arme']}",
                value=f"**Stats :** {b['stats']}\n**Talent :** {b['talent']}\n**Note :** {b['note']}",
                inline=False
            )
        await ctx.send(embed=embed)

    @elden.command(name="guide")
    async def elden_guide(self, ctx):
        embed = self.embed_base("📖 Nightreign — Guide & Tips", 0x8844CC)
        embed.description = ELDEN_NIGHTREIGN["description"]
        tips = "\n".join(ELDEN_NIGHTREIGN["tips"])
        embed.add_field(name="💡 Conseils essentiels", value=tips, inline=False)
        await ctx.send(embed=embed)

    @elden.command(name="boss")
    async def elden_boss(self, ctx):
        embed = self.embed_base("👹 Nightreign — Nightlords", 0xCC2200)
        for boss in ELDEN_NIGHTREIGN["nightlords"]:
            embed.add_field(
                name=f"💀 {boss['nom']} — Difficulté : {boss['difficulte']}",
                value=f"**Conseil :** {boss['conseil']}",
                inline=False
            )
        await ctx.send(embed=embed)

    @elden.command(name="news")
    async def elden_news(self, ctx):
        embed = self.embed_base("📰 Elden Ring — Dernières Actus", 0xFFAA00)
        embed.description = "\n\n".join(ELDEN_NEWS)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Elden(bot))
