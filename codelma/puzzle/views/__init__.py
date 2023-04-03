from __future__ import annotations

import nextcord
from typing import List

class PuzzleView(nextcord.ui.View):
    def __init__(self, author: nextcord.Member, correct_answer: str | bool):
        super().__init__()

        self.author = author
        self.correct_answer = correct_answer

        self.children:List[nextcord.ui.Button]

    # Answer checker.
    # ----------------
    async def is_answer_correct(self, interaction: nextcord.Interaction, answer):
        if self.author.id == interaction.user.id:
            if answer == self.correct_answer:
                msg = "✅ Your answer is correct!"
            else:
                msg = f"❌ Wrong! The right answer was ``{self.correct_answer}``."


            # Grey out and colour in all buttons.
            # ------------------------------------
            for item in self.children:
                item.disabled = True # Grey out.
                
                if item.label == str(self.correct_answer):
                    item.style = nextcord.ButtonStyle.green # Set colour to green if right answer.
                else:
                    item.style = nextcord.ButtonStyle.grey # Set colour to grey if wrong answer.

            await interaction.response.edit_message(
                view = self
            )


            # Send answer message.
            # ---------------------
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
from .text import Text