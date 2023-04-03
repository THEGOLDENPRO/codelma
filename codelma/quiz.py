from __future__ import annotations

from typing import List
from dataclasses import dataclass, field
from devgoldyutils import DictDataclass, LoggerAdapter

from .quiz_types import QuizTypes
from .creator import Creator

@dataclass
class Quiz(DictDataclass):
    data:dict = field(repr=False)
    python_snippet:str|None

    id:int
    creator:Creator

    type:str = field(init=False)
    question:str = field(init=False)
    options:List[str]|None = field(init=False)
    answer:int|bool = field(init=False)

    def __post_init__(self):
        self.logger = LoggerAdapter(codelma_logger, prefix=f"Quiz")
        super().__post_init__()

        self.type = self.get("type")
        self.question = self.get("question")
        self.options = self.get("options", optional=True)
        self.answer = self.get("answer")


from . import codelma_logger