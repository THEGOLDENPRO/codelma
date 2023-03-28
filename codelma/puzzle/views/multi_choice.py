import nextcord
from typing import Any, List

from . import PuzzleView

class MultiChoice(PuzzleView):
    def __init__(self, author: nextcord.Member, correct_answer: int, options:List[str]):
        super().__init__(author, correct_answer)

        self.correct_answer:int = self.children[correct_answer].label

        for option in options:
            self.add_item(
                MultiChoiceButton(
                    name = option
                )
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
        