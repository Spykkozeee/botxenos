import discord
from discord.ext import commands

COD_META = {
    "multi": {
        "S": ["HRM-9", "XM4", "Holger 26", "Model L", "Jackal PDW", "GPR 91"],
        "A": ["AK-74", "DG-58", "SVD", "MCW", "Haymaker", "Reclaimer 18"],
        "B": ["RAM-7", "Longbow", "Kastov 762", "Saug", "AS VAL"],
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

COD_BUILDS = {
    "hrm-9": {
        "attachments": ["Suppressor D20", "Barre lisse Precision-6", "EXF Lunar Grip", "Crosse HVGP-40", "Laser SL Razoredge"],
        "role": "Mobilité & TTK court"
    },
    "holger 26": {
        "attachments": ["Suppressor Shadowstrike", "Barre FTAC MSP-98", "Poignée Bruen TF45", "Chargeur 60 balles", "Crosse FSS Fortress"],
        "role": "LMG polyvalent, excellent mid-range"
    },
    "xm4": {
        "attachments": ["Suppressor D7", "Barre Dozer-90 Long", "Poignée Kombat Grip", "Crosse Bruen Archangel", "Chargeur 45 balles"],
        "role": "AR stable, méta ranked"
    },
    "model l": {
        "attachments": ["Silencieux Monolithic", "Barre 20' Talon", "Poignée Commando Foregrip", "Chargeur 50 balles", "Crosse FTAC Sport"],
        "role": "AR longue portée, excellent en ranked"
    },
    "jackal pdw": {
        "attachments": ["Suppressor Avenger", "Barre Jackal Ranger", "Laser Schlager PEQ", "Chargeur 50 balles", "Poignée Fabric Grip"],
        "role": "SMG agressif, top méta S4"
    },
    "gpr 91": {
        "attachments": ["Suppressor Harbinger D20", "Barre Tempus Haste", "Poignée Phantom Grip", "Crosse Assault-60", "Laser FSS Ole"],
        "role": "AR polyvalent, bon en pubs et ranked"
    },
    "ak-74": {
        "attachments": ["Suppressor Kastovia", "Barre 20' Spetsnaz RPK", "Poignée Phantom Grip", "Chargeur 45 balles", "Crosse Proljeće"],
        "role": "AR solide, bon recoil"
    },
    "haymaker": {
        "attachments": ["Choke Bryson Modified", "Barre 21.5' Bryson", "Poignée Phantom Grip", "Chargeur 12 balles", "Crosse Sawed Off"],
        "role": "Shotgun agressif, dévastateur en CQB"
    },
    "reclaimer 18": {
        "attachments": ["Choke Bryson Pattern", "Barre 20' SA Tyrant", "Laser Schlager PEQ", "Chargeur 8 balles", "Poignée Bruen Flash V4"],
        "role": "Shotgun semi-auto, excellent close range"
    },
    "saug": {
        "attachments": ["Suppressor Monolithic", "Barre SAUG 6.1'", "Poignée Commando Foregrip", "Chargeur 64 balles", "Laser 5MW"],
        "role": "SMG ultra rapide, idéal rush"
    },
    "longbow": {
        "attachments": ["Suppressor Shadow Strike", "Barre 26' RXM", "Poignée Phantom Grip", "Crosse Singuard Arms Whisper", "Laser Tac Laser"],
        "role": "Sniper semi-auto, parfait pour quick scope"
    },
    "svd": {
        "attachments": ["Suppressor Monolithic", "Barre 24' Tiger Team", "Scope Hybrid", "Poignée Fabric Grip", "Chargeur 20 balles"],
        "role": "DMR longue portée, idéal pour cover"
    },
    "sg-12": {
        "attachments": ["Choke Modified", "Barre 12.6' SOCOM", "Laser 5MW", "Chargeur 30 balles", "Poignée Phantom Grip"],
        "role": "Shotgun full-auto, domination en CQB"
    },
    "vst": {
        "attachments": ["Suppressor Monolithic", "Barre longue VST", "Poignée Commando", "Chargeur étendu", "Crosse légère"],
        "role": "SMG compacte, bon en mobilité"
    },
    "voyak kt-3": {
        "attachments": ["Suppressor Kastovia", "Barre Voyak 16'", "Poignée Phantom Grip", "Chargeur 45 balles", "Crosse Proljeće"],
        "role": "AR récente BO7, bon recoil et TTK"
    },
    "ram-7": {
        "attachments": ["Suppressor Harbinger", "Barre TAC R4", "Poignée Commando Foregrip", "Chargeur 60 balles", "Laser Tac Laser"],
        "role": "AR burst, efficace en mid-long range"
    },
    "kastov 762": {
        "attachments": ["Suppressor Kastovia", "Barre 20' Spetsnaz RPK", "Poignée Phantom Grip", "Chargeur 40 balles", "Crosse Proljeće"],
        "role": "AR puissante, gros dégâts par balle"
    },
    "mcw": {
        "attachments": ["Suppressor Monolithic", "Barre 16' MCW Cyclone", "Poignée Commando Foregrip", "Chargeur 60 balles", "Laser Integrated"],
        "role": "AR équilibrée, top pour débuter"
    },
    "dg-58": {
        "attachments": ["Suppressor Harbinger D20", "Barre DG-58 LS18", "Poignée Phantom Grip", "Chargeur 45 balles", "Crosse HVS 3.4 Pad"],
        "role": "AR burst 3 balles, excellent en ranked"
    },
}

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
            "`!cod build <arme>` — Build recommandé\n"
            "`!cod armes` — Liste de toutes les armes dispo"
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

    @cod.command(name="armes")
    async def cod_armes(self, ctx):
        embed = self.embed_base("🔫 COD — Armes Disponibles", 0xFFAA00)
        armes = ", ".join([f"`{k}`" for k in COD_BUILDS.keys()])
        embed.description = f"Armes avec build disponible :\n{armes}\n\nUtilise `!cod build <arme>` pour voir le build."
        await ctx.send(embed=embed)

    @cod.command(name="build")
    async def cod_build(self, ctx, *, arme: str = None):
        if arme is None:
            await ctx.send(embed=discord.Embed(
                description="Usage : `!cod build <arme>` (ex: `!cod build hrm-9`)\nTape `!cod armes` pour voir toutes les armes disponibles.",
                color=0xFF4444
            ))
            return

        key = arme.lower().strip()

        # Recherche exacte
        if key in COD_BUILDS:
            b = COD_BUILDS[key]
        else:
            # Recherche partielle
            matches = [k for k in COD_BUILDS.keys() if key in k or k in key]
            if len(matches) == 1:
                b = COD_BUILDS[matches[0]]
                key = matches[0]
            elif len(matches) > 1:
                await ctx.send(embed=discord.Embed(
                    description=f"Plusieurs armes trouvées : {', '.join([f'`{m}`' for m in matches])}\nSois plus précis !",
                    color=0xFFAA00
                ))
                return
            else:
                await ctx.send(embed=discord.Embed(
                    description=f"❌ Arme `{arme}` introuvable.\nTape `!cod armes` pour voir toutes les armes disponibles.",
                    color=0xFF4444
                ))
                return

        embed = self.embed_base(f"🔧 Build — {key.upper()}", 0xFFAA00)
        embed.add_field(name="🎯 Rôle", value=b["role"], inline=False)
        embed.add_field(name="🔩 Attachements", value="\n".join([f"• {a}" for a in b["attachments"]]), inline=False)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(COD(bot))
