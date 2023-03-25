import nextcord
import logging as log
from nextcord.ext import commands
from decouple import config
from devgoldyutils import Colours, LoggerAdapter

from codelma import Codelma, codelma_logger

codelma = Codelma()
bot_logger = LoggerAdapter(codelma_logger, prefix="BOT")

bot = commands.Bot()

# Events
# -------------
@bot.event
async def on_ready():
    bot_logger.info(Colours.GREEN.apply_to_string("[We're ready!]"))


# Commands
# -------------
@bot.slash_command(description="⭐ Begin your journey.", guild_ids=[863416692083916820]) # Added my guild id for testing, add yours too if you would like to test this command.
async def solve(interaction: nextcord.Interaction):
    await interaction.send("work in progress...", ephemeral=True)


bot.run(config("TOKEN", cast=str))