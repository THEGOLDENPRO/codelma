import nextcord
from typing import Any

from . import PuzzleView

class TrueFalse(PuzzleView):
    def __init__(self, author: nextcord.Member, correct_answer: Any):
        super().__init__(author, correct_answer)

    # Buttons
    # ----------
    @nextcord.ui.button(label="True", style=nextcord.ButtonStyle.green)
    async def true(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await self.is_answer_correct(button, interaction, True)

    @nextcord.ui.button(label="False", style=nextcord.ButtonStyle.red)
    async def false(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await self.is_answer_correct(button, interaction, False)