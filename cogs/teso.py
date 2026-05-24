import discord
from discord.ext import commands

TESO_BUILDS = {
    "dps": [
        {"classe": "Necromancer", "role": "DPS", "setup": "Staff de feu + Magie Céleste", "note": "Top DPS parsing, parfait trials"},
        {"classe": "Sorcerer", "role": "DPS Magicka", "setup": "Double Staff Inferno", "note": "Facile à jouer, excellent pour solo/vet"},
        {"classe": "Nightblade", "role": "DPS Stamina", "setup": "Dual Wield + 2H", "note": "Burst incroyable en PvP et PvE"},
    ],
    "heal": [
        {"classe": "Templar", "role": "Healer", "setup": "Restauration + Bouclier", "note": "Meilleur healer vet, indispensable en trials"},
        {"classe": "Warden", "role": "Healer", "setup": "Restauration + Animal Companions", "note": "Polyvalent, bon en donjon normal"},
    ],
    "tank": [
        {"classe": "Dragonknight", "role": "Tank", "setup": "Bouclier + 1H + Armor lourde", "note": "Meilleur tank meta, contrôle parfait"},
        {"classe": "Arcanist", "role": "Tank", "setup": "Bouclier + Cruxweave", "note": "Nouveau, très résistant avec bonne sustain"},
    ]
}

TESO_NEWS = [
    "⚔️ **Gold Road Chapter** : Scribing toujours dominant, nouvelles compétences disponibles.",
    "🔮 **Méta DPS** : Necromancer devant Sorcerer après le dernier patch 10.3.",
    "🏰 **Nouveau contenu** : Donjon 'Bedlam Veil' ajouté avec des sets exclusifs.",
    "🌍 **ESO Plus** : Nouveau jeu de base offert ce mois-ci pour les abonnés.",
]

class TESO(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def embed_base(self, title, color=0xAA6600):
        embed = discord.Embed(title=title, color=color)
        embed.set_footer(text="MALA Bot • The Elder Scrolls Online")
        return embed

    @commands.group(name="teso", invoke_without_command=True)
    async def teso(self, ctx):
        embed = self.embed_base("⚔️ TESO — Menu")
        embed.description = (
            "`!teso builds` — Builds méta par rôle\n"
            "`!teso dps` — Builds DPS\n"
            "`!teso heal` — Builds Healer\n"
            "`!teso tank` — Builds Tank\n"
            "`!teso news` — Dernières actus"
        )
        await ctx.send(embed=embed)

    @teso.command(name="builds")
    async def teso_builds(self, ctx):
        embed = self.embed_base("⚔️ TESO — Builds Méta", 0xAA6600)
        for role, builds in TESO_BUILDS.items():
            val = "\n".join([f"**{b['classe']}** — {b['note']}" for b in builds])
            embed.add_field(name=f"🔹 {role.upper()}", value=val, inline=False)
        await ctx.send(embed=embed)

    @teso.command(name="dps")
    async def teso_dps(self, ctx):
        embed = self.embed_base("⚔️ TESO — Builds DPS", 0xFF4444)
        for b in TESO_BUILDS["dps"]:
            embed.add_field(
                name=f"🗡️ {b['classe']} ({b['role']})",
                value=f"**Setup :** {b['setup']}\n**Note :** {b['note']}",
                inline=False
            )
        await ctx.send(embed=embed)

    @teso.command(name="heal")
    async def teso_heal(self, ctx):
        embed = self.embed_base("💚 TESO — Builds Healer", 0x00CC66)
        for b in TESO_BUILDS["heal"]:
            embed.add_field(
                name=f"💊 {b['classe']}",
                value=f"**Setup :** {b['setup']}\n**Note :** {b['note']}",
                inline=False
            )
        await ctx.send(embed=embed)

    @teso.command(name="tank")
    async def teso_tank(self, ctx):
        embed = self.embed_base("🛡️ TESO — Builds Tank", 0x3366FF)
        for b in TESO_BUILDS["tank"]:
            embed.add_field(
                name=f"🛡️ {b['classe']}",
                value=f"**Setup :** {b['setup']}\n**Note :** {b['note']}",
                inline=False
            )
        await ctx.send(embed=embed)

    @teso.command(name="news")
    async def teso_news(self, ctx):
        embed = self.embed_base("📰 TESO — Dernières Actualités", 0xFFAA00)
        embed.description = "\n\n".join(TESO_NEWS)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(TESO(bot))
