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
    await interaction.response.send_message("""Bonjour à toutes et tous ! Je suis le Grand Chef Grailloux ! Cuisinier depuis mon plus jeune âge, je suis à la tête des réstaurants les plus renomés du monde !
Mais en ce moment, ma carrière m'a mené dans un viel hopital où je cuisine de la pauvre purée de patate sans sel...
Mais ce n'est point gravissime ! J'espère un jour pouvoir partir de ce lieu horrifiant.
D'ailleurs, ici on m'appelle Antonoir.
||@everyone||""")
    
@bot.event
async def on_message(message):
    if message.author.bot:
        return
    
    if message.content.lower() == "!@@":
        channel = message.channel
        await message.delete()
        await channel.send("""# **RÈGLEMENT**
Ces règles sont valables pour toustes

:grey_exclamation: Ce serveur a été créé pour améliorer la communication entre tous les membres de GDM. Il est donc réservé exclusivement au projet. Des salons sont dédiés aux contenus "poubelle", qui n'a rien à voir avec le projet.

:no_entry_sign:  Comme tous bon serveur, on ne spam pas, encore moins avec des ping (@).
Le contenu échangé doit resté correct, pas explicite, gênant ou choquant
Il est important que tout le monde se respect, pas d'insultes par exemple.

:green_circle:  Ce serveur est le lieu pour poser vos questions et montrer l'avancé du projet. Pour cela il y a différents salons pour organiser le contenu du projet, respectez bien ce fonctionnement.

:fire:  Enfin, GDM est probablement voué à évoluer, de nouveaux membres pourraient rejoindre l'aventure, alors le salon #👋・présentations est le lieu parfait pour laisser une trace de vous même, dire qui vous êtes pour que les potentiel·le·s nouve·aux·lles puissent savoir qui vous êtes (en dehors du traditionnel alcooliques anonymes avec James et Eva)
||@everyone||""")
        

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    
    if message.content.lower() == "patate":
        channel = message.channel
        await message.delete()
        await channel.send("Quelqu'un à parlé de purée de patate ?! Haha ! C'est un plat dont je connais tous les détails ! Mais je vous conseil de le saler un peu...")


keep_alive()

bot.run(os.getenv('DISCORD_TOKEN'))