from attr import attrs


@attrs(auto_attribs=True)
class Armor:
    # Is this item currently identified.
    identified: bool
    quality: int
