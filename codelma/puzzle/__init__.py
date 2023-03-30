import nextcord
from devgoldyutils import LoggerAdapter

from .. import Codelma, codelma_logger
from ..quiz import Quiz
from ..quiz_types import QuizTypes

from . import views

import json, os, urllib.parse # REMOVE LATER

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

        code_block = f"""
```python
{quiz.python_snippet}
```
        """

        quiz_embed.add_field(
            name = quiz.question,
            value = (lambda: "" if quiz.python_snippet is None else code_block)()
        )

        if os.path.isfile(f"authors/{quiz.creator}.json"):
            with open(f"authors/{quiz.creator}.json", "r") as file:
                creator_data = json.load(file)
                creator_name = creator_data.get("name", quiz.creator)
                creator_url = creator_data.get("social_link")
                if creator_url:
                    creator_icon = f"https://t2.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url={urllib.parse.quote_plus(creator_url)}&size=256"
                    print(creator_icon)
                else:
                    creator_icon = f""
                quiz_embed.set_author(name=creator_name, url=creator_url, icon_url=creator_icon)
        else:
            quiz_embed.set_author(name=quiz.creator)

        quiz_embed.set_footer(
            text = f"""
ID: {quiz.creator}/{quiz.id}
"""
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
            view = views.MultiChoice(self.interaction.user, quiz.answer, quiz.options)

            await self.interaction.send(
                embed = embed, 
                view = view
            )

            return await view.wait()