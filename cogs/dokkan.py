import discord
from discord.ext import commands

DOKKAN_TEAMS = [
    {
        "nom": "Super Saiyan God SS",
        "tier": "S",
        "leader": "LR SSGSS Vegeta (Dokkan Awakened)",
        "membres": ["LR SSGSS Goku", "SSB Goku & Vegeta (EZA)", "SSGSS Gogeta", "Vegeta Blue (Int)"],
        "lien": "Super Saiyan + Shocking Speed + Godly Power",
        "conseil": "Meilleure team EZA/Transcended en 2025, domination totale."
    },
    {
        "nom": "Fusion",
        "tier": "S",
        "leader": "LR Vegito Blue",
        "membres": ["LR Gogeta Blue", "GT Gogeta", "LR Vegito (dokkan)", "Kefla"],
        "lien": "Fusion + Super Saiyan + Kamehameha",
        "conseil": "Dégâts stratosphériques, parfait pour les events difficiles."
    },
    {
        "nom": "Universe Survival",
        "tier": "A",
        "leader": "LR Android 17 & 18",
        "membres": ["LR Jiren", "Golden Frieza (US)", "Dyspo", "Hit"],
        "lien": "Universe Survival Saga + Fierce Battle",
        "conseil": "Très polyvalente, excellente pour Dokkan Events."
    },
]

DOKKAN_TIPS = [
    "💎 **Zénies** : Farm le stage '10th Anni. Super Battle Road' pour du Zeni rapide.",
    "🐉 **Dragon Stones** : Ne pull pas sur les banniéres non-featured, garde pour les LR.",
    "⚡ **EZA** : Prioritize EZA Gogeta SSJ4 et Vegito Blue — changeurs de game.",
    "🔗 **Liens** : Toujours vérifier les liens entre persos avant de build une équipe.",
    "🎯 **Events** : Le Super Battle Road donne des médailles essentielles pour les EZA.",
    "🌟 **Awakening** : Dokkan-Awakene tes LR en priorité, le boost est énorme.",
]

DOKKAN_NEWS = [
    "🎉 **Anni 10** : Nouveaux LR disponibles — LR Broly Légendaire Super Saiyan.",
    "🔥 **EZA** : EZA SSJ4 Gogeta et Vegito Blue confirmés pour ce mois.",
    "💎 **Login bonus** : 300 Dragon Stones offertes pour la semaine anniversaire.",
    "🐉 **Dokkan Festival** : Nouveau personnage UR+ en bannière limitée — 0.1% de taux.",
]

class Dokkan(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def embed_base(self, title, color=0xFF6600):
        embed = discord.Embed(title=title, color=color)
        embed.set_footer(text="MALA Bot • Dragon Ball Z Dokkan Battle")
        return embed

    @commands.group(name="dokkan", invoke_without_command=True)
    async def dokkan(self, ctx):
        embed = self.embed_base("🐉 Dokkan Battle — Menu")
        embed.description = (
            "`!dokkan teams` — Meilleures équipes méta\n"
            "`!dokkan tips` — Conseils & astuces\n"
            "`!dokkan news` — Dernières actus & events\n"
            "`!dokkan team <nom>` — Détails d'une équipe"
        )
        await ctx.send(embed=embed)

    @dokkan.command(name="teams")
    async def dokkan_teams(self, ctx):
        embed = self.embed_base("⚡ Dokkan — Teams Méta", 0xFF6600)
        for t in DOKKAN_TEAMS:
            embed.add_field(
                name=f"[{t['tier']}] {t['nom']} — Leader : {t['leader']}",
                value=t["conseil"],
                inline=False
            )
        await ctx.send(embed=embed)

    @dokkan.command(name="team")
    async def dokkan_team(self, ctx, *, nom: str = None):
        if nom is None:
            await ctx.send(embed=discord.Embed(description="Usage : `!dokkan team <nom>` (ex: `!dokkan team Fusion`)", color=0xFF4444))
            return
        t = next((t for t in DOKKAN_TEAMS if t["nom"].lower() == nom.lower()), None)
        if not t:
            noms = ", ".join([f"`{t['nom']}`" for t in DOKKAN_TEAMS])
            await ctx.send(embed=discord.Embed(description=f"❌ Équipe introuvable. Disponibles : {noms}", color=0xFF4444))
            return
        embed = self.embed_base(f"🐉 Team {t['nom']}", 0xFF8800)
        embed.add_field(name="👑 Leader", value=t["leader"], inline=False)
        embed.add_field(name="👥 Membres", value="\n".join([f"• {m}" for m in t["membres"]]), inline=False)
        embed.add_field(name="🔗 Liens clés", value=t["lien"], inline=False)
        embed.add_field(name="💡 Conseil", value=t["conseil"], inline=False)
        await ctx.send(embed=embed)

    @dokkan.command(name="tips")
    async def dokkan_tips(self, ctx):
        embed = self.embed_base("💡 Dokkan — Conseils & Astuces", 0xFFAA00)
        embed.description = "\n\n".join(DOKKAN_TIPS)
        await ctx.send(embed=embed)

    @dokkan.command(name="news")
    async def dokkan_news(self, ctx):
        embed = self.embed_base("📰 Dokkan — Dernières Actualités", 0xCC2200)
        embed.description = "\n\n".join(DOKKAN_NEWS)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Dokkan(bot))
