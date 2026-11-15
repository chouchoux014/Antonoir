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
        await message.channel.send("""# **RÈGLEMENT**
Ces règles sont valables pour toustes

​❕​ Ce serveur a été créé pour améliorer la communication entre tous les membres de GDM. Il est donc réservé exclusivement au projet. Des salons sont dédiés aux contenus "poubelle", qui n'a rien à voir avec le projet.

🚫​ Comme tous bon serveur, on ne spam pas, encore moins avec des ping (@).
Le contenu échangé doit resté correct, pas explicite, gênant ou choquant
Il est important que tout le monde se respect, pas d'insultes par exemple.

​🟢​ Ce serveur est le lieu pour poser vos questions et montrer l'avancé du projet. Pour cela il y a différents salons pour organiser le contenu du projet, respectez bien ce fonctionnement.

​🔥​ Enfin, GDM est probablement voué à évoluer, de nouveaux membres pourraient rejoindre l'aventure, alors le salon https://discord.com/channels/1571217588825096365/1571229634769715212 est le lieu parfait pour laisser une trace de vous même, dire qui vous êtes pour que les potentiel·le·s nouve·aux·lles puissent savoir qui vous êtes (en dehors du traditionnel alcooliques anonymes avec James et Eva)
||@everyone||""")

    elif contenu == "patate":
        await message.delete()
        await message.channel.send("Quelqu'un à parlé de purée de patate ?! Haha ! C'est un plat dont je connais tous les détails ! Mais je vous conseil de le saler un peu...")


keep_alive()

bot.run(os.getenv('DISCORD_TOKEN'))