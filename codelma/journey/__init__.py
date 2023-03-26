import nextcord
from devgoldyutils import LoggerAdapter

from .. import Codelma, codelma_logger
from ..quiz import Quiz
from ..quiz_types import QuizTypes

from . import views

class Journey():
    """Where you can begin a quiz."""
    def __init__(self, interaction: nextcord.Interaction, codelma: Codelma, quiz_type: QuizTypes) -> None:
        self.codelma = codelma
        self.quiz_type = quiz_type
        self.interaction = interaction

        self.logger = LoggerAdapter(codelma_logger, prefix = "Journey")

        self.embed = nextcord.Embed(
            colour = 0x2B2D31 # Invisible colour.
        )

    async def start(self):
        """Starts a quiz."""
        quiz = self.codelma.get_quiz(self.quiz_type)
        quiz_embed = self.embed.copy()

        quiz_embed.title = "• " + quiz.question 

        quiz_embed.description = f"""
```python
{quiz.python_snippet}
```
        """

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

            await view.wait()