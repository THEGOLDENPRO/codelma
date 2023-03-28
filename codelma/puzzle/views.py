import nextcord
from typing import Any, List

class TrueFalse(nextcord.ui.View):
    def __init__(self, author: nextcord.Member, correct_answer: Any):
        super().__init__()
        self.author = author
        self.correct_answer = correct_answer

    # Buttons
    # ----------
    @nextcord.ui.button(label="True", style=nextcord.ButtonStyle.green)
    async def true(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await self.is_answer_correct(button, interaction, True)

    @nextcord.ui.button(label="False", style=nextcord.ButtonStyle.grey)
    async def false(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await self.is_answer_correct(button, interaction, False)


    # Answer checker.
    # ----------------
    async def is_answer_correct(self, button: nextcord.ui.Button, interaction: nextcord.Interaction, answer):
        if self.author.id == interaction.user.id:
            if answer == self.correct_answer:
                msg = "✅ Your answer is correct!"
            else:
                msg = f"❌ Wrong! The right answer was ``{answer}``."

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


class MultiChoice(nextcord.ui.View):
    def __init__(self, author: nextcord.Member, options:List[str], correct_answer: Any):
        super().__init__()
        self.author = author
        self.correct_answer = correct_answer

        for option in options:
            self.add_item(
                MultiChoiceButton(
                    name = option
                )
            )


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
            # Triggers when a member that didn't start the quiz attempts to interact.
            await interaction.response.send_message(
                "🛑 You can only answer your own Quiz!",
                ephemeral = True
            )


class MultiChoiceButton(nextcord.ui.Button):
    def __init__(self, name:str) -> None:
        super().__init__(
            label = name,
            style = nextcord.ButtonStyle.blurple
        )

    async def callback(self, interaction: nextcord.Interaction) -> None:
        view:MultiChoice = self.view

        await view.is_answer_correct(self, interaction, self.label)
        