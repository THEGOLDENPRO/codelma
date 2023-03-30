from __future__ import annotations

from dataclasses import dataclass, field
import json
import urllib.parse
from devgoldyutils import DictDataclass, LoggerAdapter


@dataclass
class Creator(DictDataclass):
    data: dict = field(repr=False)

    id: str
    name: str = field(init=False)
    link: str = field(init=False, repr=False)
    icon: str = field(init=False, repr=False)

    def __post_init__(self):
        self.logger = LoggerAdapter(codelma_logger, prefix="Creator")
        super().__post_init__()

        with open(f"creators/{self.id}", "r", encoding="utf-8") as file:
            data = json.load(file)

        self.name = data.get("name", self.id)
        self.link = data.get("link", "https://google.com")
        self.icon = "https://t2.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON"\
            f"&fallback_opts=TYPE,SIZE,URL&url={urllib.parse.quote_plus(self.link)}&size=256"


from . import codelma_logger
