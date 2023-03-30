from __future__ import annotations

from dataclasses import dataclass, field
import json
import re
import urllib.parse
from devgoldyutils import LoggerAdapter


@dataclass
class Creator:
    id: str
    name: str = field(init=False)
    link: str = field(init=False, repr=False)
    icon: str = field(init=False, repr=False)

    def __post_init__(self):
        self.logger = LoggerAdapter(codelma_logger, prefix="Creator")

        with open(f"creators/{self.id}.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        self.name = data.get("name", self.id)
        self.link = data.get("social_link")
        if self.link:
            match_yt = re.match(
                "https?\:\/\/(www\.)?youtube\.com/channel/(.+)", self.link or "."
            )
            if match_yt and match_yt.start != match_yt.end:
                channel_id = (
                    match_yt.string.split("youtube.com/channel", 1)[1]
                    .split("?", 1)[0]
                    .split("#", 1)[0]
                )
                self.icon = f"https://banner.yt/{channel_id}/avatar"
                print(self.icon)
            else:
                self.icon = (
                    "https://t2.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON"
                    f"&fallback_opts=TYPE,SIZE,URL&url={urllib.parse.quote_plus(self.link)}&size=256"
                )
        else:
            self.link = "https://github.com/THEGOLDENPRO/codelma"
            self.icon = "https://github.com/THEGOLDENPRO/codelma/raw/master/assets/in_development.png"


from . import codelma_logger
