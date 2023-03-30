from __future__ import annotations

from typing import List
from dataclasses import dataclass, field
from devgoldyutils import DictDataclass, LoggerAdapter
import json


@dataclass
class Creator(DictDataclass):
    data: dict = field(repr=False)
    
    id: str
    name: str = field(init=False)
    social_link: str = field(init=False, repr=False)
    icon_url: str = field(init=False, repr=False)

    def __post_init__(self):
        self.logger = LoggerAdapter(codelma_logger, prefix=f"Creator")
        super().__post_init__()

        with open(f"creators/{self.id}", "r") as file:
            data = json.load(file)
        
        


from . import codelma_logger
