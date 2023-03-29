from __future__ import annotations

from typing import List
from dataclasses import dataclass, field
from devgoldyutils import DictDataclass, LoggerAdapter

from .quiz_types import QuizTypes

@dataclass
class Quiz(DictDataclass):
    data:dict = field(repr=False)
    python_snippet:str|None

    creator:str

    id:str = field(init=False)
    type:str = field(init=False)
    question:str = field(init=False)
    options:List[str]|None = field(init=False)
    answer:int|bool = field(init=False)

    def __post_init__(self):
        self.logger = LoggerAdapter(codelma_logger, prefix=f"Quiz")
        super().__post_init__()

        self.id = str(self.get("id"))
        self.type = self.get("type")
        self.question = self.get("question")
        self.options = (lambda: None if self.type == QuizTypes.TRUE_FALSE.name.lower() else self.get("options"))()
        self.answer = self.get("answer")


from . import codelma_logger