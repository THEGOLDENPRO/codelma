from __future__ import annotations

import nextcord
from typing import List

class PuzzleView(nextcord.ui.View):
    def __init__(self, author: nextcord.Member, correct_answer: int | str | bool):
        super().__init__()

        self.author = author
        self.correct_answer = correct_answer

        self.children:List[nextcord.ui.Button]

    # Answer checker.
    # ----------------
    async def is_answer_correct(self, button: nextcord.ui.Button, interaction: nextcord.Interaction, answer):
        if self.author.id == interaction.user.id:
            if answer == self.correct_answer:
                msg = "✅ Your answer is correct!"
            else:
                msg = f"❌ Wrong! The right answer was ``{self.correct_answer}``."

            # Grey out button.
            # -----------------
            for item in self.children:
                item.disabled = True

            await interaction.response.edit_message(
                view = self
            )


            await interaction.followup.send(
                content = msg
            )

            self.stop()
            

        else:
            await interaction.response.send_message(
                "🛑 You can only answer your own Quiz!",
                ephemeral = True
            )


from .true_false import TrueFalse
from .multi_choice import MultiChoice