from enum import Enum

class QuizTypes(Enum):
    MULTIPLE_CHOICE = 0
    TRUE_FALSE = 1
    TEXT = 2

    def __init__(self, colour_value:str):
        ...