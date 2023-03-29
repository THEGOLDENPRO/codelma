from __future__ import annotations

import os
import json
import random
import logging as log
from decouple import config
from typing import Dict, Tuple, List
from devgoldyutils import Colours, add_custom_handler, LoggerAdapter

codelma_logger = add_custom_handler(
    log.getLogger(Colours.PINK_GREY.apply_to_string("CODELMA"))
)
codelma_logger.setLevel(getattr(log, config("LOG_LEVEL", default="INFO")))

from .quiz import Quiz
from .quiz_types import QuizTypes

class Codelma():
    """The main class. Allows you to retrieve quizzes."""
    def __init__(self) -> None:
        self.logger = LoggerAdapter(codelma_logger, prefix="Codelma")

        self.__quizzes:Dict[str, List[Tuple[dict, str|None, str]]] = {}
        
        for type in QuizTypes:
            self.__quizzes[type.name.lower()] = []

        self.global_quiz_count = 0

        self.__load_quizzes()


    def get_quiz(self, type: QuizTypes | str) -> Quiz:
        """Returns a random quiz from that type."""
        if isinstance(type, QuizTypes):
            type = type.name

        quiz = random.choice(self.__quizzes[type.lower()])
        return Quiz(quiz[0], quiz[1], quiz[2])

    def get_quizzes(self, type: QuizTypes | str) -> List[Quiz]:
        """Returns a list of quizzes from that type."""
        if isinstance(type, QuizTypes):
            type = type.name
        
        return [Quiz(quiz[0], quiz[1], quiz[2]) for quiz in self.__quizzes[type.lower()]]
    

    # If you wondering what the underscore is for, these are just private methods that are used internally in this class and are not be used externally.
    # ------------------------------------------------------------------------------------------------------------------------------------------------------
    def __load_quizzes(self):
        """Method that looks for all quizzes and loads/caches them within this class. Usually ran after bot is ready."""
        self.__clear_cache()

        for author in os.listdir("./quizzes"):

            id_count = 0
            not_loaded_count = 0
            for file in os.listdir(f"./quizzes/{author}"):

                if os.path.splitext(file)[1] == ".json":
                    id_count += 1
                    self.logger.debug(Colours.PINK_GREY.apply_to_string(f"Loading {author}/{id_count}..."))

                    json_config:dict = json.load(open(f"./quizzes/{author}/{id_count}.json"))
                    
                    # If the 'omit_code' json key is not set to true, we will search for a python code snippet.
                    # -------------------------------------------------------------------------------------------
                    python_code_snippet:str|None = None

                    if json_config.get("omit_code", False) is False:

                        try:
                            python_code_snippet:str = open(f"./quizzes/{author}/{id_count}.py", mode="r").read()
                        except FileNotFoundError as e:
                            self.logger.error(
                                f"We got a FileNotFoundError when loading quiz '{author}/{id_count}'. Make sure 'omit_code' is set to true if you wish to not include code snippet.\n" + 
                                f"Error >> {e}"
                            )

                    # Appending the quiz dict and python code to the appropriate type list in cache.
                    # -------------------------------------------------------------------------------
                    type:str|None = json_config.get("type")

                    if not type is None:

                        try:

                            self.__quizzes[type.lower()].append(
                                (json_config, python_code_snippet, author)
                            )

                        except KeyError as e:
                            self.logger.error(
                                f"We got a KeyError when loading quiz '{author}/{id_count}'. The type may be incorrectly typed or spelt, please check it.\n" + 
                                f"Error >> {e}"
                            )

                    else:
                        not_loaded_count += 1
                        self.logger.error(
                            f"The quiz '{author}/{id_count}' does not contain a type so it will NOT be loaded."
                        )

            self.global_quiz_count += (id_count - not_loaded_count)
            self.logger.info(f"Loaded {Colours.ORANGE + str(id_count - not_loaded_count) + Colours.RESET_COLOUR} quizzes from '{author}'s.")

    def __clear_cache(self) -> None:
        """Method that clears the cache."""
        for type in self.__quizzes:
            self.__quizzes[type] = []
        
        self.logger.debug("Cleared quizzes cache!")