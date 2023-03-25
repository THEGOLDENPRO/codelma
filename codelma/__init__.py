import os
import json
import logging as log
from typing import Dict, Tuple, List
from devgoldyutils import Colours, add_custom_handler, LoggerAdapter, pprint

codelma_logger = add_custom_handler(
    log.getLogger(Colours.PINK_GREY.apply_to_string("CODELMA"))
)
codelma_logger.setLevel(log.DEBUG)


class Codelma():
    """The main class. Allows you to retrieve quizzes."""
    def __init__(self) -> None:
        self.logger = LoggerAdapter(codelma_logger, prefix="Codelma")

        self.__quizzes:Dict[str, List[Tuple[dict, str]]] = {
            "multipleChoice" : []
        }

        self.__load_quizzes()

    

    # If you wondering what the underscore is for, these are just private methods that are used internally in this class and are not be used externally.
    # ------------------------------------------------------------------------------------------------------------------------------------------------------
    def __load_quizzes(self):
        """Method that looks for all quizzes and loads/caches them within this class. Usually ran after bot is ready."""
        self.__clear_cache()

        for author in os.listdir("./quizzes"):

            id_count = 0
            for file in os.listdir(f"./quizzes/{author}"):

                if os.path.splitext(file)[1] == ".json":
                    id_count += 1

                    json_config:dict = json.load(open(f"./quizzes/{author}/{id_count}.json"))
                    python_code_snippet:str = open(f"./quizzes/{author}/{id_count}.py", mode="r").read()

                    try:

                        self.__quizzes[json_config["type"]].append(
                            (json_config, python_code_snippet)
                        )

                    except KeyError as e:
                        self.logger.error(
                            f"We got a KeyError when loading quiz '{author}/{id_count}'. Something may be incorrectly typed or spelt.\n" + 
                            f"Error >> {e}"
                        )

            self.logger.debug(f"Cached '{author}'s quizzes.")

    def __clear_cache(self) -> None:
        """Method that clears the cache."""
        for type in self.__quizzes:
            self.__quizzes[type] = []
        
        self.logger.debug("Cleared quizzes cache!")