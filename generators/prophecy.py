from typing import Optional

from generators.rarity import generate_rarity
from models.prophecy import Prophecy


def generate_prophecy(text: str) -> Optional[Prophecy]:
    text = text.strip()
    name = text.splitlines()[1]
    rarity = generate_rarity(text=text)
    return Prophecy(
        name=name,
        rarity=rarity
    )



