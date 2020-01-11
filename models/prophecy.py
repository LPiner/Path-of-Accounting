from typing import Optional

from attr import attrs, attrib

from enums.rarity import Rarity


@attrs(auto_attribs=True)
class Prophecy:
    name: str
    rarity: Rarity
