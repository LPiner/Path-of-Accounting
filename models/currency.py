from typing import Optional

from attr import attrs, attrib

from enums.rarity import Rarity


@attrs(auto_attribs=True)
class Currency:
    type: str
    rarity: Rarity = attrib(default=Rarity.CURRENCY, init=False)
