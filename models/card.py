from attr import attrs, attrib

from enums.rarity import Rarity


@attrs(auto_attribs=True)
class Card:
    type: str
    rarity: Rarity = attrib(default=Rarity.DIVINATION_CARD, init=False)
