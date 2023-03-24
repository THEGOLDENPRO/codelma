import nextcord
from nextcord.ext import commands
from decouple import config

bot = commands.Bot()


@bot.slash_command(description="Replies with pong!")
async def ping(interaction: nextcord.Interaction):
    await interaction.send("Pong!", ephemeral=True)


def start():
    bot.run(config("TOKEN", cast=str))