from __future__ import annotations

import nextcord
from nextcord.ext import commands
from decouple import config
from devgoldyutils import Colours, LoggerAdapter

from codelma import Codelma, codelma_logger
from codelma.puzzle import Puzzle
from codelma.quiz_types import QuizTypes

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
@bot.slash_command(name="solve", description="🧩 Begin your puzzle.", guild_ids=[863416692083916820, 883443159798018078, 1077682705552121920]) # Added my guild id for testing, add yours too if you would like to test this command.
async def solve(
    interaction: nextcord.Interaction, 
    type: int = nextcord.SlashOption(
        name = "quiz_type",
        choices = {
            "Multiple Choice": 0, 
            "True or False": 1
        }, 
        required = False)
    ):

    if type is None:
        type = 0
    
    quiz_type = QuizTypes(type)

    puzzle = Puzzle(interaction, codelma, quiz_type)

    await puzzle.start()


bot.run(config("TOKEN", cast=str))