from __future__ import annotations

from dataclasses import dataclass, field
import json
import re
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
            match_gh = re.match(
                "https?://(www\.)?github\.com/.+", self.link
            )
            match_yt_channel = re.match(
                "https?://(www\.)?youtube\.com/channel/.+", self.link
            )
            match_yt_handle = re.match(
                "https?://(www\.)?youtube\.com/@.+", self.link
            )
            match_yt_c = re.match(
                "https?://(www\.)?youtube\.com/c/.+", self.link
            )
            if match_gh and match_gh.start != match_gh.end:
                username = match_gh.string.rsplit("/", 1)[1]
                userdata = requests.get(f"https://api.github.com/users/{username}", timeout=30).json()
                self.icon = userdata["avatar_url"]
            elif match_yt_channel and match_yt_channel.start != match_yt_channel.end:
                channel_id = (
                    match_yt_channel.string.split("youtube.com/channel", 1)[1]
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
            elif match_yt_c and match_yt_c.start != match_yt_c.end:
                c_id = (
                    match_yt_c.string.split("youtube.com/c/", 1)[1]
                    .split("?", 1)[0]
                    .split("#", 1)[0]
                )
                channel_data = requests.get(f"https://yt.lemnoslife.com/channels?cId={c_id}", timeout=30).json()
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
