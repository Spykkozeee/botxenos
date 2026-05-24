import discord
from discord.ext import commands

DBD_KILLERS = [
    {"nom": "Nurse", "tier": "S", "pouvoir": "Blink (téléportation)", "perks_meta": ["Pop Goes the Weasel", "Scourge Hook: Pain Resonance", "Corrupt Intervention"], "conseil": "Apprends les Blinks, elle domine toutes les maps"},
    {"nom": "Blight", "tier": "S", "pouvoir": "Lethal Rush (charges)", "perks_meta": ["Pop Goes the Weasel", "STBFL", "Rapid Brutality"], "conseil": "Excellent sur maps complexes, très technique"},
    {"nom": "Wesker", "tier": "A", "pouvoir": "Uroboros Infection", "perks_meta": ["Scourge Hook: Pain Resonance", "Deadlock", "Nowhere to Hide"], "conseil": "Bon début pour nouveaux joueurs killer"},
    {"nom": "Huntress", "tier": "A", "pouvoir": "Hatchets (à distance)", "perks_meta": ["Scourge Hook", "Dragon's Grip", "Corrupt Intervention"], "conseil": "Top sur maps ouvertes, difficile à maîtriser"},
]

DBD_SURVIVORS = [
    {"nom": "Sable Ward", "tier": "A", "perks_bonus": ["Distortion", "Dark Theory"], "conseil": "Perks très défensifs, bon pour débutants"},
    {"nom": "Dwight Fairfield", "tier": "B", "perks_bonus": ["Leader", "Prove Thyself"], "conseil": "Orienté soutien d'équipe"},
    {"nom": "Claudette Morel", "tier": "A", "perks_bonus": ["Empathy", "Botany Knowledge"], "conseil": "Meilleure healeuse, indispensable en SWF"},
]

DBD_META_PERKS = {
    "killer": ["Pop Goes the Weasel", "Scourge Hook: Pain Resonance", "Corrupt Intervention", "Deadlock", "Nowhere to Hide"],
    "survivor": ["Dead Hard", "Borrowed Time", "Windows of Opportunity", "Decisive Strike", "Unbreakable"],
}

DBD_NEWS = [
    "🔪 **Chapitre 36** : Nouveau killer et survivor ajoutés, map inédite.",
    "⚖️ **Balance patch** : Dead Hard légèrement nerfé, Corrupt Intervention inchangé.",
    "🎯 **Ranked** : Nouveau mode compétitif avec classement ELO en test.",
    "🧪 **PTB** : Remaniement des générateurs en test sur le serveur public.",
]

class DBD(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def embed_base(self, title, color=0xCC0000):
        embed = discord.Embed(title=title, color=color)
        embed.set_footer(text="MALA Bot • Dead by Daylight")
        return embed

    @commands.group(name="dbd", invoke_without_command=True)
    async def dbd(self, ctx):
        embed = self.embed_base("🔪 Dead by Daylight — Menu")
        embed.description = (
            "`!dbd killers` — Tier list killers méta\n"
            "`!dbd survivors` — Tier list survivors\n"
            "`!dbd perks` — Perks méta killer & survivor\n"
            "`!dbd killer <nom>` — Infos détaillées d'un killer\n"
            "`!dbd news` — Dernières actus & patches"
        )
        await ctx.send(embed=embed)

    @dbd.command(name="killers")
    async def dbd_killers(self, ctx):
        embed = self.embed_base("🔪 DBD — Tier List Killers", 0xCC0000)
        for k in DBD_KILLERS:
            embed.add_field(
                name=f"[{k['tier']}] {k['nom']} — {k['pouvoir']}",
                value=k["conseil"],
                inline=False
            )
        await ctx.send(embed=embed)

    @dbd.command(name="survivors")
    async def dbd_survivors(self, ctx):
        embed = self.embed_base("🏃 DBD — Tier List Survivors", 0x0088CC)
        for s in DBD_SURVIVORS:
            embed.add_field(
                name=f"[{s['tier']}] {s['nom']}",
                value=f"**Perks bonus :** {', '.join(s['perks_bonus'])}\n{s['conseil']}",
                inline=False
            )
        await ctx.send(embed=embed)

    @dbd.command(name="perks")
    async def dbd_perks(self, ctx):
        embed = self.embed_base("⚙️ DBD — Perks Méta", 0xAA4400)
        embed.add_field(
            name="🔪 Killer — Top Perks",
            value="\n".join([f"• {p}" for p in DBD_META_PERKS["killer"]]),
            inline=False
        )
        embed.add_field(
            name="🏃 Survivor — Top Perks",
            value="\n".join([f"• {p}" for p in DBD_META_PERKS["survivor"]]),
            inline=False
        )
        await ctx.send(embed=embed)

    @dbd.command(name="killer")
    async def dbd_killer_info(self, ctx, *, nom: str = None):
        if nom is None:
            await ctx.send(embed=discord.Embed(description="Usage : `!dbd killer <nom>` (ex: `!dbd killer Nurse`)", color=0xFF4444))
            return
        k = next((k for k in DBD_KILLERS if k["nom"].lower() == nom.lower()), None)
        if not k:
            noms = ", ".join([f"`{k['nom']}`" for k in DBD_KILLERS])
            await ctx.send(embed=discord.Embed(description=f"❌ Killer introuvable. Disponibles : {noms}", color=0xFF4444))
            return
        embed = self.embed_base(f"🔪 {k['nom']} — Détails", 0xCC0000)
        embed.add_field(name="⚡ Pouvoir", value=k["pouvoir"], inline=True)
        embed.add_field(name="🏆 Tier", value=k["tier"], inline=True)
        embed.add_field(name="⚙️ Perks Méta", value="\n".join([f"• {p}" for p in k["perks_meta"]]), inline=False)
        embed.add_field(name="💡 Conseil", value=k["conseil"], inline=False)
        await ctx.send(embed=embed)

    @dbd.command(name="news")
    async def dbd_news(self, ctx):
        embed = self.embed_base("📰 DBD — Dernières Actualités", 0xFFAA00)
        embed.description = "\n\n".join(DBD_NEWS)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(DBD(bot))
