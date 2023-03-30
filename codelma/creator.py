from __future__ import annotations

from dataclasses import dataclass, field
import json
import re
import time
import urllib.parse
from devgoldyutils import LoggerAdapter
import requests


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
            match_yt_handle = re.match(
                "https?\:\/\/(www\.)?youtube\.com/@(.+)", self.link or "."
            )
            match_yt_clink = re.match(
                "https?\:\/\/(www\.)?youtube\.com/c/(.+)", self.link or "."
            )
            if match_yt and match_yt.start != match_yt.end:
                channel_id = (
                    match_yt.string.split("youtube.com/channel", 1)[1]
                    .split("?", 1)[0]
                    .split("#", 1)[0]
                )
                self.icon = f"https://www.banner.yt/{channel_id}/avatar"
            elif match_yt_handle and match_yt_handle.start != match_yt_handle.end:
                handle = (
                    match_yt_handle.string.split("youtube.com/@", 1)[1]
                    .split("?", 1)[0]
                    .split("#", 1)[0]
                )
                channel_data = requests.get(f"https://yt.lemnoslife.com/channels?handle=@{handle}", timeout=30).json()
                channel_id = channel_data["items"][0]["id"]
                self.icon = f"https://www.banner.yt/{channel_id}/avatar"
            elif match_yt_clink and match_yt_clink.start != match_yt_clink.end:
                c_id = (
                    match_yt_clink.string.split("youtube.com/c/", 1)[1]
                    .split("?", 1)[0]
                    .split("#", 1)[0]
                )
                channel_data = requests.get(f"https://yt.lemnoslife.com/channels?cId=@{c_id}", timeout=30).json()
                channel_id = channel_data["items"][0]["id"]
                self.icon = f"https://www.banner.yt/{channel_id}/avatar"
            else:
                self.icon = (
                    "https://t2.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON"
                    f"&fallback_opts=TYPE,SIZE,URL&url={urllib.parse.quote_plus(self.link)}&size=256"
                )
        else:
            self.link = "https://github.com/THEGOLDENPRO/codelma"
            self.icon = "https://github.com/THEGOLDENPRO/codelma/raw/master/assets/placeholder_icon"


from . import codelma_logger
