import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from keep_alive import keep_alive

load_dotenv()

print("Lancement du BOT...")
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot connecté")
    try:
        synced = await bot.tree.sync()
        print(f"commandes synchronisées : {len(synced)}")
    except Exception as e:
        print(f"Erreur lors de la synchronisation des commandes : {e}")


@bot.tree.command(name="jaaj", description="Envoi du message prédéfini")
async def jaaj(interaction: discord.Interaction):
       await interaction.response.send_message("Commande indisponible.")
    
@bot.event
async def on_message(message):
    if message.author.bot:
        return

    contenu = message.content.lower()

    if contenu == "!!jaaj":
        await message.delete()
        await message.channel.send("Commande désactivée")

    elif contenu == "patate":
        await message.delete()
        await message.channel.send("Quelqu'un à parlé de purée de patate ?! Haha ! C'est un plat dont je connais tous les détails ! Mais je vous conseil de le saler un peu...")


keep_alive()

bot.run(os.getenv('DISCORD_TOKEN'))
