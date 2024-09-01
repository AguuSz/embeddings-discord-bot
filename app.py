import os
from dotenv import load_dotenv
import discord
from discord import app_commands
from discord.ext import commands

load_dotenv()  # Carga el contenido de .env

bot = commands.Bot(command_prefix="!!", intents=discord.Intents.default())


@bot.event
async def on_ready():
    print("El bot está listo")
    print(
        f"Invita al bot con el siguiente enlace: {discord.utils.oauth_url(bot.user.id)}"
    )
    try:
        synced = await bot.tree.sync()
        print(f"Se sincronizaron {len(synced)} comandos")
    except Exception as e:
        print(f"Fallo al sincronizar los comandos: {e}")


@bot.tree.command(
    name="vx",
    description="Reemplaza la URL de Twitter/X con la URL de VXTwitter para mejor visualización.",
)
@app_commands.describe(url="La URL de Twitter/X que se va a reemplazar")
async def replaceurl(interaction: discord.Interaction, url: str):
    if "twitter.com" in url or "x.com" in url:
        new_url = url.replace("twitter.com", "vxtwitter.com").replace(
            "x.com", "vxtwitter.com"
        )
        await interaction.response.send_message(new_url)
    else:
        await interaction.response.send_message(
            "URL tan invalida como vos.", ephemeral=True
        )


token = os.getenv("DISCORD_BOT_TOKEN")
bot.run(token)
