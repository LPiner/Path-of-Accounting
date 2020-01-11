from typing import Optional

from attr import attrs, attrib

from enums.rarity import Rarity


@attrs(auto_attribs=True)
class Map:

    type: str

    identified: bool
    rarity: Rarity
    tier: int
    ilvl: int

    blighted: bool
    shaper: bool
    elder: bool
    enslaver: bool
    eradicator: bool
    constrictor: bool
    purifier: bool

    quality: Optional[int] = attrib(default=None)
    iiq: Optional[int] = attrib(default=None)
    iir: Optional[int] = attrib(default=None)
    pack_size: Optional[int] = attrib(default=None)
    name: Optional[str] = attrib(default=None)
