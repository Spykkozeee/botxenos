import discord
from discord.ext import commands
import asyncio
from datetime import datetime

# Stockage temporaire des LFG actifs (en mémoire)
lfg_sessions = {}

JEUX_VALIDES = ["cod", "teso", "elden", "dbd", "dokkan"]

class LFG(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def embed_base(self, title, color=0x5865F2):
        embed = discord.Embed(title=title, color=color)
        embed.set_footer(text="MALA Bot • LFG System")
        return embed

    @commands.group(name="lfg", invoke_without_command=True)
    async def lfg(self, ctx):
        embed = self.embed_base("👥 LFG — Looking For Group")
        embed.description = (
            "`!lfg create <jeu> <nb_joueurs> [description]` — Créer un LFG\n"
            "`!lfg list [jeu]` — Voir les LFG actifs\n"
            "`!lfg join <id>` — Rejoindre un LFG\n"
            "`!lfg leave <id>` — Quitter un LFG\n"
            "`!lfg close <id>` — Fermer ton LFG\n\n"
            f"**Jeux disponibles :** {', '.join(JEUX_VALIDES)}"
        )
        await ctx.send(embed=embed)

    @lfg.command(name="create")
    async def lfg_create(self, ctx, jeu: str = None, nb_joueurs: int = None, *, description: str = "Pas de description"):
        if jeu is None or nb_joueurs is None:
            await ctx.send(embed=discord.Embed(
                description="Usage : `!lfg create <jeu> <nb_joueurs> [description]`\nEx : `!lfg create cod 3 On cherche un 3ème pour Warzone !`",
                color=0xFF4444
            ))
            return

        jeu = jeu.lower()
        if jeu not in JEUX_VALIDES:
            await ctx.send(embed=discord.Embed(
                description=f"❌ Jeu invalide. Jeux valides : {', '.join(JEUX_VALIDES)}",
                color=0xFF4444
            ))
            return

        if nb_joueurs < 1 or nb_joueurs > 10:
            await ctx.send(embed=discord.Embed(description="❌ Nombre de joueurs entre 1 et 10.", color=0xFF4444))
            return

        session_id = f"{ctx.author.id}-{int(datetime.now().timestamp())}"
        lfg_sessions[session_id] = {
            "createur": ctx.author,
            "jeu": jeu,
            "nb_max": nb_joueurs,
            "membres": [ctx.author],
            "description": description,
            "channel": ctx.channel.id,
            "cree_le": datetime.now().strftime("%H:%M")
        }

        embed = self.embed_base(f"👥 LFG — {jeu.upper()}", 0x57F287)
        embed.description = f"**{ctx.author.display_name}** cherche des joueurs !"
        embed.add_field(name="🎮 Jeu", value=jeu.upper(), inline=True)
        embed.add_field(name="👥 Joueurs", value=f"1/{nb_joueurs}", inline=True)
        embed.add_field(name="🕐 Créé à", value=lfg_sessions[session_id]["cree_le"], inline=True)
        embed.add_field(name="📝 Description", value=description, inline=False)
        embed.add_field(name="🔑 ID", value=f"`{session_id}`", inline=False)
        embed.set_footer(text=f"MALA Bot • LFG | !lfg join {session_id}")

        msg = await ctx.send(embed=embed)
        lfg_sessions[session_id]["message_id"] = msg.id
        await msg.add_reaction("✅")

    @lfg.command(name="list")
    async def lfg_list(self, ctx, jeu: str = None):
        sessions = lfg_sessions
        if jeu:
            sessions = {k: v for k, v in sessions.items() if v["jeu"] == jeu.lower()}

        if not sessions:
            await ctx.send(embed=discord.Embed(
                description="Aucun LFG actif pour le moment. Crée-en un avec `!lfg create` !",
                color=0xFFAA00
            ))
            return

        embed = self.embed_base("👥 LFG — Sessions Actives", 0x5865F2)
        for sid, s in list(sessions.items())[:10]:
            membres_noms = ", ".join([m.display_name for m in s["membres"]])
            embed.add_field(
                name=f"🎮 {s['jeu'].upper()} — {len(s['membres'])}/{s['nb_max']} joueurs",
                value=f"**Créateur :** {s['createur'].display_name}\n**Membres :** {membres_noms}\n**ID :** `{sid}`",
                inline=False
            )
        await ctx.send(embed=embed)

    @lfg.command(name="join")
    async def lfg_join(self, ctx, session_id: str = None):
        if session_id is None or session_id not in lfg_sessions:
            await ctx.send(embed=discord.Embed(description="❌ ID de session invalide. Utilise `!lfg list` pour voir les sessions.", color=0xFF4444))
            return

        s = lfg_sessions[session_id]
        if ctx.author in s["membres"]:
            await ctx.send(embed=discord.Embed(description="❌ Tu es déjà dans ce LFG !", color=0xFF4444))
            return

        if len(s["membres"]) >= s["nb_max"]:
            await ctx.send(embed=discord.Embed(description="❌ Ce LFG est complet !", color=0xFF4444))
            return

        s["membres"].append(ctx.author)
        complet = len(s["membres"]) >= s["nb_max"]

        embed = self.embed_base(f"✅ {ctx.author.display_name} a rejoint le LFG !", 0x57F287 if not complet else 0xFFAA00)
        embed.add_field(name="🎮 Jeu", value=s["jeu"].upper(), inline=True)
        embed.add_field(name="👥 Joueurs", value=f"{len(s['membres'])}/{s['nb_max']}", inline=True)
        membres_noms = ", ".join([m.display_name for m in s["membres"]])
        embed.add_field(name="👤 Membres", value=membres_noms, inline=False)

        if complet:
            embed.description = "🎉 **Le groupe est complet ! Bonne partie à tous !**"

        await ctx.send(embed=embed)

    @lfg.command(name="leave")
    async def lfg_leave(self, ctx, session_id: str = None):
        if session_id is None or session_id not in lfg_sessions:
            await ctx.send(embed=discord.Embed(description="❌ ID de session invalide.", color=0xFF4444))
            return

        s = lfg_sessions[session_id]
        if ctx.author not in s["membres"]:
            await ctx.send(embed=discord.Embed(description="❌ Tu n'es pas dans ce LFG.", color=0xFF4444))
            return

        s["membres"].remove(ctx.author)
        await ctx.send(embed=discord.Embed(
            description=f"✅ Tu as quitté le LFG **{s['jeu'].upper()}**.",
            color=0x57F287
        ))

    @lfg.command(name="close")
    async def lfg_close(self, ctx, session_id: str = None):
        if session_id is None or session_id not in lfg_sessions:
            await ctx.send(embed=discord.Embed(description="❌ ID de session invalide.", color=0xFF4444))
            return

        s = lfg_sessions[session_id]
        if s["createur"].id != ctx.author.id:
            await ctx.send(embed=discord.Embed(description="❌ Seul le créateur peut fermer ce LFG.", color=0xFF4444))
            return

        del lfg_sessions[session_id]
        await ctx.send(embed=discord.Embed(
            description=f"✅ LFG **{s['jeu'].upper()}** fermé par {ctx.author.display_name}.",
            color=0x57F287
        ))

async def setup(bot):
    await bot.add_cog(LFG(bot))
