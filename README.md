# 🤖 MALA Bot — Discord Gaming Bot

Bot Discord pour le serveur MALA couvrant **COD, TESO, Elden Ring Nightreign, DBD et Dokkan Battle**.

---

## 📦 Installation

### 1. Prérequis
- **Python 3.10+** — [Télécharger Python](https://www.python.org/downloads/)
- Un **token de bot Discord**

### 2. Cloner / Télécharger le projet
Place tous les fichiers dans un dossier `mala-bot/`.

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. Configurer le token
Crée un fichier `.env` à la racine du projet (copie `.env.example`) :
```
DISCORD_TOKEN=ton_token_ici
```
Remplace `ton_token_ici` par ton vrai token Discord.

### 5. Lancer le bot
```bash
python bot.py
```

---

## 🔧 Structure du projet

```
mala-bot/
├── bot.py              # Fichier principal
├── requirements.txt    # Dépendances
├── .env                # Token (ne pas partager !)
└── cogs/
    ├── cod.py          # Call of Duty
    ├── teso.py         # The Elder Scrolls Online
    ├── elden.py        # Elden Ring Nightreign
    ├── dbd.py          # Dead by Daylight
    ├── dokkan.py       # Dokkan Battle
    ├── lfg.py          # Looking For Group
    └── help.py         # Aide
```

---

## 🎮 Commandes disponibles

### 🔫 Call of Duty
| Commande | Description |
|----------|-------------|
| `!cod meta` | Tier list armes multi (S/A/B/C) |
| `!cod zombies` | Stratégie et builds Zombies |
| `!cod news` | Dernières actus & patches |
| `!cod build <arme>` | Build recommandé (ex: `!cod build hrm-9`) |

### ⚔️ TESO
| Commande | Description |
|----------|-------------|
| `!teso builds` | Tous les builds méta |
| `!teso dps` | Builds DPS |
| `!teso heal` | Builds Healer |
| `!teso tank` | Builds Tank |
| `!teso news` | Dernières actus |

### 🌙 Elden Ring Nightreign
| Commande | Description |
|----------|-------------|
| `!elden builds` | Builds méta complets |
| `!elden guide` | Guide Nightreign + tips |
| `!elden boss` | Nightlords et conseils |
| `!elden news` | Dernières actus |

### 🔪 Dead by Daylight
| Commande | Description |
|----------|-------------|
| `!dbd killers` | Tier list killers |
| `!dbd survivors` | Tier list survivors |
| `!dbd perks` | Top perks méta |
| `!dbd killer <nom>` | Détails d'un killer (ex: `!dbd killer Nurse`) |
| `!dbd news` | Dernières actus |

### 🐉 Dokkan Battle
| Commande | Description |
|----------|-------------|
| `!dokkan teams` | Meilleures équipes méta |
| `!dokkan team <nom>` | Détails d'une équipe |
| `!dokkan tips` | Conseils & astuces |
| `!dokkan news` | Dernières actus & events |

### 👥 LFG — Looking For Group
| Commande | Description |
|----------|-------------|
| `!lfg create <jeu> <nb> [desc]` | Créer un LFG |
| `!lfg list [jeu]` | Voir les LFG actifs |
| `!lfg join <id>` | Rejoindre un LFG |
| `!lfg leave <id>` | Quitter un LFG |
| `!lfg close <id>` | Fermer son LFG |

---

## 🔑 Configurer le bot sur Discord

1. Va sur [discord.com/developers/applications](https://discord.com/developers/applications)
2. Clique **New Application** → donne un nom
3. Va dans **Bot** → clique **Add Bot**
4. Dans **Privileged Gateway Intents**, active :
   - ✅ `SERVER MEMBERS INTENT`
   - ✅ `MESSAGE CONTENT INTENT`
5. Copie le **Token** → colle-le dans `.env`
6. Va dans **OAuth2 > URL Generator** :
   - Scopes : `bot`, `applications.commands`
   - Permissions : `Send Messages`, `Embed Links`, `Read Message History`, `Add Reactions`
7. Copie le lien généré et invite le bot sur ton serveur

---

## 🚀 Héberger le bot 24/7 (optionnel)

- **[Railway.app](https://railway.app)** — Gratuit, simple à configurer
- **[Render.com](https://render.com)** — Gratuit avec un peu de config
- **VPS** (Hostinger, OVH...) — Lance avec `python bot.py` dans un screen/tmux

---

*MALA Bot — Fait pour le serveur MALA 🎮*
