import nextcord
from nextcord.ext import commands
from decouple import config

bot = commands.Bot()


@bot.slash_command() # Just a basic ping command I added to test to see if the bot was working. (Will remove later.)
async def ping(interaction: nextcord.Interaction):
    await interaction.send("Pong!", ephemeral=True)


bot.run(config("TOKEN", cast=str))