import nextcord
import logging as log
from nextcord.ext import commands
from decouple import config
from devgoldyutils import Colours, LoggerAdapter, add_custom_handler

codelma_logger = add_custom_handler(
    log.getLogger(Colours.PINK_GREY.apply_to_string("CODELMA"))
)

bot = commands.Bot()

# Events
# -------------
@bot.event
async def on_ready():
    # TODO: Place the quiz lookup method here once done.
    
    codelma_logger.info(Colours.GREEN.apply_to_string("[We're ready!]"))


# Commands
# -------------
@bot.slash_command(description="⭐ Begin your journey.", guild_ids=[863416692083916820]) # Added my guild id for testing, add yours too if you would like to test this command.
async def solve(interaction: nextcord.Interaction):
    await interaction.send("work in progress...", ephemeral=True)


codelma_logger.setLevel(log.DEBUG)
bot.run(config("TOKEN", cast=str))