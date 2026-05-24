import discord
from discord.ext import commands
from discord import app_commands

COD_META = {
    "multi": {
        "S": ["HRM-9", "XM4", "Holger 26", "Model L"],
        "A": ["AK-74", "DG-58", "SVD", "MCW"],
        "B": ["RAM-7", "Longbow", "Kastov 762"],
        "C": ["FTAC Recon", "Chimera", "FR 5.56"],
    },
    "zombies": {
        "meilleure_arme": "RAI K-84",
        "strategie": "Pack-a-Punch dès la round 15, utilisez les Perk-a-Colas dans cet ordre : Jugger-Nog, Speed Cola, Quick Revive, Stamin-Up.",
        "builds_top": [
            {"nom": "RAI K-84 Raygun", "atouts": "Dégâts extrêmes, parfait rounds 30+"},
            {"nom": "HRM-9 SMG", "atouts": "Mobilité max, idéal pour exfiltrer"},
            {"nom": "MCW Full-Auto", "atouts": "Polyvalent, bon dès le début"},
        ]
    }
}

COD_NEWS = [
    "🔫 **Saison 4** : Nouvelle carte 6v6 'Skidrow Remastered' ajoutée.",
    "🧟 **Zombies** : Nouveaux Œufs de Pâques sur Liberty Falls disponibles.",
    "⚡ **Méta Multi** : Le HRM-9 et le Holger 26 dominent après le dernier patch.",
    "🎯 **Ranked** : Système de placement revu — 10 matchs de placement pour la S4.",
]

class COD(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def embed_base(self, title, color=0xFF6600):
        embed = discord.Embed(title=title, color=color)
        embed.set_footer(text="MALA Bot • Call of Duty")
        return embed

    @commands.group(name="cod", invoke_without_command=True)
    async def cod(self, ctx):
        embed = self.embed_base("🔫 Call of Duty — Menu")
        embed.description = (
            "`!cod meta` — Tier list armes multi\n"
            "`!cod zombies` — Stratégie & builds Zombies\n"
            "`!cod news` — Dernières actu & patches\n"
            "`!cod build <arme>` — Build recommandé"
        )
        await ctx.send(embed=embed)

    @cod.command(name="meta")
    async def cod_meta(self, ctx):
        embed = self.embed_base("🔫 COD Multi — Tier List Armes", 0xFF6600)
        for tier, armes in COD_META["multi"].items():
            embed.add_field(
                name=f"**Tier {tier}**",
                value=" • ".join(armes),
                inline=False
            )
        embed.set_footer(text="MALA Bot • Méta mis à jour Saison 4")
        await ctx.send(embed=embed)

    @cod.command(name="zombies")
    async def cod_zombies(self, ctx):
        data = COD_META["zombies"]
        embed = self.embed_base("🧟 COD Zombies — Stratégie & Builds", 0x00AA44)
        embed.add_field(name="🏆 Meilleure arme", value=data["meilleure_arme"], inline=False)
        embed.add_field(name="📋 Stratégie", value=data["strategie"], inline=False)
        builds_text = "\n".join([f"**{b['nom']}** — {b['atouts']}" for b in data["builds_top"]])
        embed.add_field(name="⚔️ Builds Top", value=builds_text, inline=False)
        await ctx.send(embed=embed)

    @cod.command(name="news")
    async def cod_news(self, ctx):
        embed = self.embed_base("📰 COD — Dernières Actualités", 0x3399FF)
        embed.description = "\n\n".join(COD_NEWS)
        await ctx.send(embed=embed)

    @cod.command(name="build")
    async def cod_build(self, ctx, *, arme: str = None):
        builds = {
            "hrm-9": {"attachments": ["Suppressor D20", "Barre lisse Precision-6", "EXF Lunar Grip", "Crosse HVGP-40", "Laser SL Razoredge"], "role": "Mobilité & TTK court"},
            "holger 26": {"attachments": ["Suppressor Shadowstrike", "Barre FTAC MSP-98", "Poignée Bruen TF45", "Chargeur 60 balles", "Crosse FSS Fortress"], "role": "LMG polyvalent, excellent mid-range"},
            "xm4": {"attachments": ["Suppressor D7", "Barre Dozer-90 Long", "Poignée Kombat Grip", "Crosse Bruen Archangel", "Chargeur 45 balles"], "role": "AR stable, méta ranked"},
        }
        if arme is None:
            await ctx.send(embed=discord.Embed(description="Usage : `!cod build <arme>` (ex: `!cod build hrm-9`)", color=0xFF4444))
            return
        key = arme.lower()
        if key not in builds:
            available = ", ".join([f"`{k}`" for k in builds.keys()])
            await ctx.send(embed=discord.Embed(description=f"❌ Arme introuvable. Disponibles : {available}", color=0xFF4444))
            return
        b = builds[key]
        embed = self.embed_base(f"🔧 Build — {arme.upper()}", 0xFFAA00)
        embed.add_field(name="🎯 Rôle", value=b["role"], inline=False)
        embed.add_field(name="🔩 Attachements", value="\n".join([f"• {a}" for a in b["attachments"]]), inline=False)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(COD(bot))
