import nextcord
from devgoldyutils import LoggerAdapter

from .. import Codelma, codelma_logger
from ..quiz import Quiz
from ..quiz_types import QuizTypes

from . import views

class Puzzle():
    """Where you can begin a quiz."""
    def __init__(self, interaction: nextcord.Interaction, codelma: Codelma, quiz_type: QuizTypes) -> None:
        self.codelma = codelma
        self.quiz_type = quiz_type
        self.interaction = interaction

        self.logger = LoggerAdapter(codelma_logger, prefix = "Puzzle")

        self.embed = nextcord.Embed(
            colour = 0x2B2D31 # Invisible colour.
        )
        self.embed.title = "🧩 Solve!"

    async def start(self):
        """Starts a quiz."""
        quiz = self.codelma.get_quiz(self.quiz_type)
        quiz_embed = self.embed.copy()

        quiz_embed.add_field(
            name = quiz.question,
            value = f"""
```python
{quiz.python_snippet}
```
            """
        )

        quiz_embed.set_footer(
            text = f"Author: {quiz.creator}"
        )

        await self.send_quiz(quiz_embed, quiz)


    async def send_quiz(self, embed: nextcord.Embed, quiz: Quiz):

        if quiz.type == QuizTypes.TRUE_FALSE.name.lower():
            view = views.TrueFalse(self.interaction.user, quiz.answer)
        
            await self.interaction.send(
                embed = embed, 
                view = view
            )

            return await view.wait()

        if quiz.type == QuizTypes.MULTIPLE_CHOICE.name.lower():
            # TODO: NOT IMPLEMENTED YET!
            await self.interaction.send(
                "*Work in progress, currently only true_false works...*"
            )