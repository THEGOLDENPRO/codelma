import nextcord
from typing import Any

from . import PuzzleView

class TextModal(nextcord.ui.Modal):
    def __init__(self, view: PuzzleView):
        self.view = view
        super().__init__(
            "✍ Type your answer."
        )

        self.text = nextcord.ui.TextInput(
            label = "Text Input:",
            style = nextcord.TextInputStyle.short
        )
        self.add_item(self.text)

    async def callback(self, interaction: nextcord.Interaction) -> None:
        await self.view.is_answer_correct(interaction, self.text.value)


class Text(PuzzleView):
    def __init__(self, author: nextcord.Member, correct_answer: Any):
        super().__init__(author, correct_answer)

    # Buttons
    # ----------
    @nextcord.ui.button(label="Answer", style=nextcord.ButtonStyle.blurple, emoji="✏")
    async def answer(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_modal(TextModal(self))