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
        await channel.send("""Bonjour à toutes et tous ! Je suis le Grand Chef Grailloux ! Cuisinier depuis mon plus jeune âge, je suis à la tête des réstaurants les plus renomés du monde !
Mais en ce moment, ma carrière m'a mené dans un vieil hopital où je cuisine de la pauvre purée de patate sans sel...
Mais ce n'est point gravissime ! J'espère un jour pouvoir partir de ce lieu horrifiant.
D'ailleurs, ici on m'appelle Antonoir. Je suis là pour veiller sur vous haha !
||@everyone||""")

keep_alive()

bot.run(os.getenv('DISCORD_TOKEN'))