import nextcord
from typing import Any

class TrueFalse(nextcord.ui.View):
    def __init__(self, author: nextcord.Member, correct_answer: Any):
        super().__init__()
        self.author = author
        self.correct_answer = correct_answer

    # Buttons
    # ----------
    @nextcord.ui.button(label="True", style=nextcord.ButtonStyle.green)
    async def true(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await self.is_answer_correct(interaction, True)

    @nextcord.ui.button(label="False", style=nextcord.ButtonStyle.grey)
    async def false(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await self.is_answer_correct(interaction, False)


    # Answer checker.
    # ----------------
    async def is_answer_correct(self, interaction: nextcord.Interaction, answer):
        if self.author.id == interaction.user.id:
            if answer == self.correct_answer:
                await interaction.response.send_message("✅ Your answer is correct!")
            else:
                await interaction.response.send_message("❌ Your answer is wrong!")

            self.stop()

        else:
            await interaction.response.send_message(
                "**🛑 You can only answer your own Quiz!**"
            )